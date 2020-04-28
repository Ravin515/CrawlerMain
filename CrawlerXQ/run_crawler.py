import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
# running the different spiders seperately
#spider_name = 'xq_cube_info' #                 SP/ZH    Done    需要开代理！
#spider_name = 'xq_cube_rb'#                       ZH       需要开代理！
#spider_name = 'xq_cube_ret'#                   SP/ZH Done       需要开代理！  
#spider_name = 'xq_user_fans'#             Done        不用开代理！
#spider_name = 'xq_user_follow'#          Done       不用开代理！
#spider_name = 'xq_user_info'#              Done       不用开代理！
#spider_name = 'xq_user_info_weibo'#     Done         需要开代理！
#spider_name = 'xq_user_stock'#            Done        不用开代理！
spider_name = 'xq_user_cube'#             Done        不用开代理！
#spider_name = 'xq_user_cmt'#               Done       需要开代理！
process.crawl(spider_name)
process.start()
