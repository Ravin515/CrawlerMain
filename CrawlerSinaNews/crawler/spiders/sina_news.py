from scrapy.spiders import Spider
from scrapy import Request
from crawler.items import SinaNewsItem
from crawler.settings import *
from crawler.spiders import util
from datetime import datetime
import json
import time
import re
import copy

class SinaNewsSpider(Spider):
    name = "sina_news"
    logger = util.set_logger(name, LOG_FILE_SINANEWS)
    handle_httpstatus_list = [404]

    def start_requests(self):
        # 新闻类别 lid 取值 (2510:国内,2511:国际,2669:社会,2512:体育,2513:娱乐,2514:军事,2515:科技,2516:财经,2517:股市,2518:美股)
        channel_list = {'2510':'国内','2511':'国际','2669':'社会','2512':'体育','2513':'娱乐','2514':'军事','2515':'科技','2516':'财经','2517':'股市','2518':'美股'}
        for lid in channel_list.keys():
            lid = "2516"

            #设置起始时间和终止时间的时间戳
            etime = time.strptime("2018-10-01 00:00:00", "%Y-%m-%d %H:%M:%S")
            stime = time.strptime("2019-01-02 00:00:00", "%Y-%m-%d %H:%M:%S")
            etime = int(time.mktime(etime))
            stime = int(time.mktime(stime))
            etime = str(etime)
            stime = str(stime)
            ctime = stime

            # channel 
            channel = {'title':channel_list[lid], 'id':lid, 'cType':'lid', 'url':''}
        
            start_url = "https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=%s&etime=%s&stime=%s&ctime=%s&k=&num=50&page=1" % (lid,etime,stime,ctime)
            yield Request(url = start_url, meta = {'start_url' : start_url, 'channel' : channel}, callback = self.parse_page)

    def parse_page(self, response):
        js = json.loads(response.body)
        if js['result']['total'] % 50:
            page_total = js['result']['total']//50 + 1
        else:
            page_total = js['result']['total']//50
        start_url = response.meta['start_url']
        start_url = start_url.rstrip('1')

        for i in range(1, page_total + 1):
            url = start_url + str(i)
            yield Request(url = url,meta = {'channel' : response.meta['channel']}, callback = self.parse)

    def parse(self, response):
        js = json.loads(response.body.decode(response.encoding))
        for i in js['result']['data']:
            item = SinaNewsItem()
            item['content'] = {}
            #api中有好几个time，此处选择ctime
            item['content']['time'] = datetime.fromtimestamp(int(i['ctime']))
            # author, source, keywords, title, news_id, type, pic, channel
            item['content']['author'] = i['author']
            item['content']['source'] = i['media_name']
            item['content']['keywords'] = i['keywords']
            item['content']['title'] = i['title']
            item['content']['news_id'] = i['docid']
            item['content']['type'] = i['categoryid']
            item['content']['pic'] = i['images']
            item['content']['channel'] = response.meta['channel']
            # cmt_id
            cmt_id = {}
            cmtid = re.search('(.+?):(.+):',i['commentid'])
            if cmtid:
                cmt_id['channel'] = cmtid.group(1)
                cmt_id['comment_id'] = cmtid.group(2)
                item['content']['cmt_id'] = cmt_id
            # url
            url = i['url']
            item['content']['url'] = url
            # reply number
            if 'comment_show' in i:
                replynum = int(i['comment_show'])
            else:
                replynum = 0

            yield Request(url = url, meta={'item':item,'cmt_id':cmt_id,'replynum':replynum}, callback = self.parse_content)

    def parse_content(self, response):
        if response.status == 200:
            item = response.meta['item']

            tags = response.xpath('//head/*[@name = "tags"]/@content').extract()      
            if tags:
                item['content']['tags'] = tags[0]

            #article create / update / publish time  
            create = response.xpath('//head/*[@name = "weibo: article:create_at"]/@content').extract()      
            if create:
                item['content']['news_create_time'] = create[0]
            update = response.xpath('//head/*[@name = "weibo: article:update_at"]/@content').extract()      
            if update:
                item['content']['news_update_time'] = update[0]
            publish = response.xpath('//head/*[@property = "article:published_time"]/@content').extract()      
            if publish:
                item['content']['news_publish_time'] = publish[0]

            #parse content
            content = response.xpath('//*[@id="artibody"]/p/text()').extract()
            if content:
                item['content']['content'] = "\n".join(content)
        
            #parse reply
            replynum = response.meta['replynum']
            cmt_id = response.meta['cmt_id']
            if replynum & ('channel' in cmt_id):
                #计算reply api的页数
                if replynum % 20:
                    rptotal = replynum // 20 + 1
                else:
                    rptotal = replynum // 20
                
                page = 1
                cmt_url = 'http://comment5.news.sina.com.cn/page/info?format=json&channel=%s&newsid=%s&page='%(cmt_id['channel'], cmt_id['comment_id'])
                reply_url = cmt_url + str(page)
                reply = {}
                yield Request(url = reply_url, meta = {'item' : item, 'page' : page, 'rptotal' : rptotal, 'cmt_url' : cmt_url, 'reply' : reply}, callback = self.parse_reply)
            else:
                yield item
        elif response.status == 404:
            self.logger.error("Page 404: %s" % (response.url))
            return

    def parse_reply(self, response):
        item = response.meta['item']
        page = response.meta['page']
        rptotal = response.meta['rptotal']
        cmt_url = response.meta['cmt_url']
        reply = response.meta['reply']

        d_json = json.loads(response.body.decode(response.encoding))
        if 'cmntlist' in d_json['result']:
            if 'reply' in item['content']:
                item['content']['reply']['reply_content'].extend(d_json['result']['cmntlist'])
            else:
                if 'count' in d_json['result']:
                    reply['replynum'] = d_json['result']['count']['show']
                    reply['hotness'] = d_json['result']['count']['total']
                    reply['qreply'] = d_json['result']['count']['qreply']
                item['content']['reply'] = reply
                item['content']['reply']['reply_content'] = d_json['result']['cmntlist']

        if page == rptotal:
            yield item
        else:
            reply_url = cmt_url + str(page+1)
            yield Request(url = reply_url, meta = {'item' : item, 'page' : page + 1, 'rptotal' : rptotal, 'cmt_url' : cmt_url, 'reply' : reply}, callback = self.parse_reply)



