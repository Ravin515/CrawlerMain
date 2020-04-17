# -*- coding: utf-8 -*-
from crawler.spiders import util
from scrapy.spiders import Spider
from datetime import datetime
from scrapy import Request
from scrapy.utils.request import request_fingerprint
from crawler.items import XQItem
from crawler.settings import *
from datetime import datetime
import time
import json
import re


class XQCubeRBSpider(Spider):
    start_at=datetime.now()
    name = 'xq_cube_rb'
    logger = util.set_logger(name, LOG_FILE_CUBE_RB)
    handle_httpstatus_list = [400]

    cube_type = 'SP'
    # 上次维护的时间，每次更新
    start_time = time.strptime("2020-01-01", "%Y-%m-%d")

    def start_requests(self):
        zh_url = 'https://xueqiu.com/cubes/rebalancing/history.json?count=50&page=1&cube_symbol='
        sp_url = 'https://xueqiu.com/service/tc/snowx/PAMID/cubes/rebalancing/history?count=20&page=1&cube_symbol='


        # get start url from MongoDB
        db = util.set_mongo_server()
        symbols = []

        for s in db.xq_cube_info.find({'cube_type':self.cube_type}, {'symbol': 1, '_id': 0}):
            symbols.append(s['symbol'])
        symbols = list(set(symbols))

        # iterate each symbol
        all_page_n = len(symbols)
        for i in range(all_page_n):
            symbol = symbols[i].strip()
            now_page_n = i

            if self.cube_type == 'SP':
                url = sp_url + symbol
            elif self.cube_type == 'ZH':
                url = zh_url + symbol

            # 进度条
            if i%500==0:
                self.logger.info('%s (%s / %s) %s%%' % (symbol, str(now_page_n), str(all_page_n), str(round(float(now_page_n) / all_page_n * 100, 1))))

            yield Request(url = url,
                      callback = self.parse, meta = {'cube_type':self.cube_type, 'symbol':symbol,'page':1})


    def parse(self, response):
        try:
            if response.status == 200 and str(response.url) != "https://xueqiu.com/service/captcha":
                
                cube_type =  response.meta['cube_type']
                symbol =  response.meta['symbol']
                page = response.meta['page']

                body = re.sub('[\s]', '', response.body.decode('utf-8'))
                body = json.loads(body)

                if body['maxPage']:
                    max_page = body['maxPage']
                 
                if body['list']:
                    page_first_time = body['list'][0]['updated_at']
                    page_first_time = time.gmtime(page_first_time / 1000)
                    if page_first_time < self.start_time:
                        return
                    else:
                        for i in body['list']:
                            item = XQItem()
                            # i is of type dict
                            i['cube_symbol'] = symbol
                            i['cube_type'] = cube_type
                            item['url'] = response.url
                            item['content'] = i
                            item['fp'] = request_fingerprint(response.request)
                            yield item

                    # Second + page
                    if page < max_page:
                        page = page + 1
                        page_string =  '&page=' + str(page)
                        url = re.sub(r'&page=(\d+)', page_string, response.url)
                        yield Request(url = url, meta = {'cube_type':cube_type, 'symbol':symbol, 'page':page}, callback = self.parse)
            elif str(response.url) == "https://xueqiu.com/service/captcha":
                self.logger.error('CAPTURE ERROR: %s' % (response.meta['symbol']))

        except Exception as ex:
            self.logger.error('Parse Exception: %s %s' % (str(ex), response.url))
            #self.logger.info(str(response.body))



