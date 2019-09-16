import json
import random
import requests
from cookiespool.db import *
from cookiespool.config import *
from requests.exceptions import ConnectionError

class ValidTester(object):
    def __init__(self, website='default'):
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)
    
    def test(self, username, cookies):
        raise NotImplementedError
    
    def run(self):
        cookies_groups = self.cookies_db.all()
        for username, cookies in cookies_groups.items():
            self.test(username, cookies)


class XueqiuValidTester(ValidTester):
    def __init__(self, website='xueqiu'):
        ValidTester.__init__(self, website)
    
    def test(self, username, cookies):
        print('正在测试Cookies', '用户名', username)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('Cookies不合法', username)
            self.cookies_db.delete(username)
            print('删除Cookies', username)
            return
        try:
            test_url = TEST_URL
            headers = {'User-Agent':random.choice(USER_AGENTS)}
            response = requests.get(test_url, cookies=cookies, timeout=10, allow_redirects=False, headers = headers)
            if response.status_code == 200:
                print('Cookies有效', username)
            else:
                print(response.status_code, response.headers)
                print('Cookies失效', username)
                self.cookies_db.delete(username)
                print('删除Cookies', username)
        except ConnectionError as ex:
            print('发生异常')

if __name__ == '__main__':
    XueqiuValidTester().run()
