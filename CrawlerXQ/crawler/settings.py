# -*- coding: utf-8 -*-

# Scrapy settings for crawler_test project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CrawlerXQ'
SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# User agent
USER_AGENTS = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",] 

# Downloader middleware
DOWNLOADER_MIDDLEWARES = {
    'crawler.middleware.RandomRequestHeaders': 100,
    'crawler.middleware.CustomHttpTunnelMiddleware': 200,
}

# Download delay
DOWNLOAD_DELAY = 2

# Auto Throttle
AUTO_THROTTLE_ENABLE = False
AUTO_THROTTLE_START_DELAY = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 64
CONCURRENT_REQUESTS = 64
CONCURRENT_ITEMS = 1000




# Retry
RETRY_PRIORITY_ADJUST = -1
RETRY_ENABLED = True 
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 460]
RETRY_PRIORITY_ADJUST = -1

# Proxy
HTTPPROXY_DELAY = 1


# Pipelines
ITEM_PIPELINES = {'crawler.pipelines.MongoPipeline': 100, 
}

# Cookies settings
DOWNLOADER_STATS = True
COOKIES_ENABLED = True
COOKIES_DEBUG = False
COOKIES = [{
    #每次更新数据都需要更新cookies！！
    #登陆cookie
    #除抓SP的RB和RET，其余都要用登陆cookies！！！！,抓cmt时要用到多个 cookies！！
    #李锐1
    #'xq_a_token': 'e70965f6f42f3bbc5da6cbd6f85cfa16ca94adfc',
    #'xq_r_token': '3b995ce3d2b51ba87575f3ba7a6e83d0ad655c09'
    
    #李锐2
    #'xq_a_token': 'e029b4f540f31c5be07b34078fb2da5951583f2d',
    #'xq_r_token': '7887f44183ce16c88e8cde15a506b8f9b2135ce3'

    #俞嘉炜1
    #'xq_a_token': '668d3197161bd1a6eff003331cde4a8ef73e38e7',
    #'xq_r_token': 'c21252196a9adc011c58b52ac549c10fefc227bb'

    #俞嘉炜2
    #'xq_a_token': '844d797a48670311981a03793f1cdab22c5a246d',
    #'xq_r_token': '08670fece89dd1b71b5b735c8708ce64d3d2b842 '

    #俞嘉炜3
    'xq_a_token': '3cbfb297b5f1ffa313e858b6f34c5056f9972c12',
    'xq_r_token': 'c4e66858d090b76d7cf846c8ad5451cb4e594a1e'

    #祝宇
    #'xq_a_token': '800caafc7fb8e868b966cba35030d2ac73947616',
    #'xq_r_token': '00f02b8db37375ac965ee83bfcdaf250f333fe05'    

    #林依洋
    #'xq_a_token': '51b7711e12b877baf9b7c3f93dc5636187722afe',
    #'xq_r_token': '79bdbe6895750c55f28cd3338217ef0e1d567510'

    #非登陆cookie
    #抓SP的RB和RET时候，要用非登陆cookies！！！！
    #'xq_a_token': '8dd2cc84915c45983930bb32e788dc93e0fcfddd',
    #'xq_r_token': '5bb4c968b369150a382906ceba61eb8763282a13'
}]



# Log
# 不能写入LOG_FILE，因为LOG_FILE是root
LOG_LEVEL = 'INFO'
LOG_STDOUT = True
LOG_FILE_CUBE_INFO = 'cube_info.log' 
LOG_FILE_CUBE_RB = 'cube_rb.log' 
LOG_FILE_CUBE_RET = 'cube_ret.log' 
LOG_FILE_USER_INFO = 'user_info.log' 
LOG_FILE_USER_STOCK = 'user_stock.log' 
LOG_FILE_USER_GUANZHU = 'user_guanzhu.log' 
LOG_FILE_USER_FENSI = 'user_fensi.log' 
LOG_FILE_USER_STATUS = 'user_status.log'
LOG_FILE_PROXY = 'proxy.log'
LOG_FILE_PIPELINE = 'pipeline.log' 
LOG_FILE_MIDDLEWARE = 'log-Middleware.log'



# MongoDB settings
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27018
MONGODB_DBNAME = 'XQ-1901'

# Redis
# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Default requests serializer is pickle, but it can be changed to any module
# with loads and dumps functions. Note that pickle is not compatible between
# python versions.
# Caveat: In python 3.x, the serializer must return strings keys and support
# bytes as values. Because of this reason the json or msgpack module will not
# work by default. In python 2.x there is no such issue and you can use
# 'json' or 'msgpack' as serializers.
#SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

# Schedule requests using a priority queue. (default)
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

# Alternative queues.
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
#SCHEDULER_IDLE_BEFORE_CLOSE = 10

# Store scraped item in redis for post-processing.
#ITEM_PIPELINES = {
#    'scrapy_redis.pipelines.RedisPipeline': 300
#}

# The item pipeline serializes and stores the items in this redis key.
#REDIS_ITEMS_KEY = '%(spider)s:items'

# The items serializer is by default ScrapyJSONEncoder. You can use any
# importable path to a callable object.
#REDIS_ITEMS_SERIALIZER = 'json.dumps'

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

#Whether to flush redis queue on start
SCHEDULER_FLUSH_ON_START = False

# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
#REDIS_URL = 'redis://user:pass@hostname:9001'

# Custom redis client parameters (i.e.: socket timeout, etc.)
#REDIS_PARAMS  = {}
# Use custom redis client class.
#REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# If True, it uses redis' ``SPOP`` operation. You have to use the ``SADD``
# command to add URLs to the redis queue. This could be useful if you
# want to avoid duplicates in your start urls list and the order of
# processing does not matter.
#REDIS_START_URLS_AS_SET = False

# Default start urls key for RedisSpider and RedisCrawlSpider.
#REDIS_START_URLS_KEY = '%(name)s:start_urls'

# Use other encoding than utf-8 for redis.
#REDIS_ENCODING = 'latin1'
