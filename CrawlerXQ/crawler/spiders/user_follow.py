# -*- coding: utf-8 -*-
from crawler.spiders import util
from scrapy.spiders import Spider
from datetime import datetime
from scrapy import Request
from scrapy.utils.request import request_fingerprint
from crawler.items import XQItem
from crawler.settings import *
import json
import time

import re

class XQUserGuanzhu(Spider):
    start_at=datetime.now()
    name = 'xq_user_follow'
    logger = util.set_logger(name, LOG_FILE_USER_GUANZHU)
    #handle_httpstatus_list = [404]
    # 上次维护的时间，每次更新
    start_time = time.strptime("2020-01-01", "%Y-%m-%d")

    def start_requestss(self):
        start_url="http://xueqiu.com/friendships/groups/members.json?count=200&gid=0&uid="

        # get start url from MongoDB
        db = util.set_mongo_server()
        owner_ids = []
        for id in db.xq_cube_info.find({},{'owner_id': 1, '_id': 0}):
            owner_ids.append(id['owner_id'])
        owner_ids = list(set(owner_ids))

        # iterate each symbol
        all_page_n = len(owner_ids)
        for i in range(all_page_n):
            now_page_n = i
            owner_id = owner_ids[i]
            url = start_url+str(owner_id)

            # progress
            if i%1000==0:
                self.logger.info('%s (%s / %s) %s%%' % (owner_id, str(now_page_n), str(all_page_n), str(round(float(now_page_n) / all_page_n * 100, 1))))     

            yield Request(url = url,
                        meta = {'user_id': owner_id},
                        callback = self.parse)

    def parse(self, response):
        try:
            if response.status == 200 and str(response.url) != "https://xueqiu.com/service/captcha":
                content = json.loads(response.body.decode('utf-8'))
                if content['maxPage']:
                    max_page = content['maxPage']



                    # First page, use parse_gz
                    for item in self.parse_gz(response = response):
                        yield item

                    # Second + page, use parse_gz
                    if max_page > 1:
                        for i in range(2, max_page + 1):
                            url = response.url + '&page=' + str(i)
                            yield Request(url = url,
                                          meta = {'user_id': response.meta['user_id']},
                                          callback = self.parse_gz)

            if str(response.url) == "https://xueqiu.com/service/captcha":
                self.logger.error('CAPTURE ERROR: User ID %s' % (response.meta['user_id']))

        except Exception as ex:
            self.logger.warn('Parse Exception: %s %s' % (str(ex), response.url))

    def parse_gz(self, response):
        try:
            body = json.loads(response.body.decode('utf-8'))
            content = {}
            content['user_id'] = response.meta['user_id']

            users = []
            for user in body['users']:
                users.append(user['id'])
            content['follow'] = users
            content['lastcrawl'] = int(time.time())

            item = XQItem()
            item['url'] = response.url
            item['content'] = content

            item['fp'] = request_fingerprint(response.request)
            yield item

        except Exception as ex:
            self.logger.warn('Parse Exception: %s %s' % (str(ex), response.url))
