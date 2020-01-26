
#website
WEBSITE = 'xueqiu'

# Headers
USER_AGENTS = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27018
MONGODB_DBNAME = 'Proxy'

# Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

#是否启用代理
PROXY_ENABLED = False
# 代理服务器,讯代理购买固定ip
PROXY = [
    {
        'PROXYHOST' : '122.114.36.243',
        'PROXYPORT' : 23128,
        'PROXYUSER' : '5cdoqbzcyk',
        'PROXYPASS' : 'tuhpljuuzl'
        },
    {
        'PROXYHOST' : "118.89.192.96",
        'PROXYPORT' : 23128,
        'PROXYUSER' : "nhfkriwg8e",
        'PROXYPASS' : "3nl7aruttq"
        },
    {
        'PROXYHOST' : "47.104.79.229",
        'PROXYPORT' : 23128,
        'PROXYUSER' : "xzwud7ager",
        'PROXYPASS' : "jrp9nignuj"
        }
    ]



#Log信息
LOG_LEVEL = 'INFO'
LOG_FILE_LOGIN = 'login.log'


# API地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5000

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = False
# API接口服务
API_PROCESS = True

#账户文件
#ACCOUNTS_FILE = 'accounts.txt'
ACCOUNTS_FILE = 'accounts.txt'

# 循环周期
CYCLE = 21600


GENERATOR_MAP = {
    'xueqiu': 'XQCookiesGenerator'
}

TEST_URL = 'https://xueqiu.com/P/SP1000524'




