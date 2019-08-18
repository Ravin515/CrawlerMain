import time
from multiprocessing import Process
from cookiespool.api import app
from cookiespool.config import *
from cookiespool.tester import *
from cookiespool.generator import *
from accounts.importer import *


class Scheduler(object):

    @staticmethod
    def generate_cookie(cycle=CYCLE):
        print('Cookies生成进程开始运行')
        try:
            generator = XQCookiesGenerator(WEBSITE)
            generator.run()
            print('Cookies生成完成')
            time.sleep(cycle)
        except Exception as ex:
            print(ex.args)


    @staticmethod
    def api():
        print('API接口开始运行')
        app.run(host=API_HOST, port=API_PORT)
    
    def run(self):
        importer = Import()
        importer.scan()

        if API_PROCESS:
            api_process = Process(target=Scheduler.api)
            api_process.start()
        
        if GENERATOR_PROCESS:
            generate_process = Process(target=Scheduler.generate_cookie)
            generate_process.start()
        
        if VALID_PROCESS:
            valid_process = Process(target=Scheduler.valid_cookie)
            valid_process.start()


    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print('Cookies检测进程开始运行')
            try:
                    tester = XueqiuValidTester().run()
                    tester.run()
                    print('Cookies检测完成')
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)
