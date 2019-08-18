from login.login import CookiesGenerate
from accounts.importer import Import
from cookiespool.scheduler import Scheduler
from cookiespool.tester import XueqiuValidTester


#username = '13455863320'
#password = 'px274586'

def main():
    s = Scheduler()
    s.run()
    #l = CookiesGenerate(username,password)
    #cookie = l.main()

    


if __name__ == '__main__':
    main()
