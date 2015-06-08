#!/usr/bin/python
print "program started"
import os
import logging
logging.basicConfig(filename='testlog.log',level=logging.DEBUG)
import traceback
import datetime
import time
logging.debug("filestarted imported")
from threading import Timer
def dingprinter():
    print "ding"
    raise
def processkiller():
    process.kill()

def writetolog():
    Timer(5,dingprinter).start()
    while 1:

        logging.debug(str(datetime.datetime.now()))
        time.sleep(1)
        print "something"


from multiprocessing import Process
print "program got further"
import sys
def makeproc():
    process=Process(target=writetolog)
    process.start()


if __name__ == '__main__':

    process=Process(target=writetolog)
    process.start()


    print "evenfurther"
    Timer(3,process.terminate).start()
    print "after timer"
    pid=process.pid

    print "i printed"
    print pid
    sys.stdout.flush()
    print "i stopped"
    Timer(6,makeproc).start()

    #process.terminate() # works on Windows only



#os.sytem('kill -9 {}'.format(pid)) # my replacements on Linux
"""
import time
cwd=os.getcwd()
os.mkdir(cwd+"/testdir")

while True:
    logging.debug("here im logingincrap")
    time.sleep(1)
    pass
"""
