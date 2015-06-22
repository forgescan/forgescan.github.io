#!/usr/bin/python
# -*- coding: cp1252 -*-
import os
os.chdir("/home/ubuntu/forgescan.github.io/")

import logging

from fileIO import *
from HAPYAKFUNCTIONS import *
import traceback


logfile=open("/home/ubuntu/forgescan.github.io/demomaker.log","w")
logfile.close()

logging.basicConfig(filename='demomaker.log',level=logging.DEBUG)
logging.debug("HERE I SHOULD BE LOGGING SOMTHING")



from threading import Thread


import threading




import gspread002
import time
import sys
from threading import Timer
from multiprocessing import Process
  



import threading

import ctypes

import time
import traceback



THREAD_TERMINATE = 1 # Privilege level for termination
import datetime
def timeout():

    logging.debug("timeout, no new thread made"+str(datetime.datetime.now()))
    
import subprocess
#from multiprocessing import Process
import multiprocessing

#print "program got further"
import sys
def makeproc():
    process=Process(target=writetolog)
    process.start()
class SheetCheckerThread():#multiprocessing.Process):

    def __init__(self):
        self.sheetchecker=gspread002.GoogleDocsSession()
        print self.sheetchecker.checkwhenupdated()

    def checksheet(self):
        lastcheck=self.sheetchecker.lastworksheetupdate
        self.sheetchecker.updatecell("U2",str(lastcheck))
        consoleinput=str(self.sheetchecker.currentworksheet.acell("v2"))
        if consoleinput!="<Cell R2C22 'Command Recieved'>":
            self.sheetchecker.updatecell("V2",str("Command Recieved"))

        print consoleinput
        if "~UPDATESCREENSHOTS" in consoleinput:
            os.system("sudo python screenshottaker.py &")
        if "~UPDATE~" in consoleinput:
            pass

        if "~CMD~" in consoleinput:
            pass
            consoleinput=consoleinput.replace("~CMD~","")
            consoleinput=consoleinput.replace("<Cell R2C22 '","")
            consoleinput=consoleinput.replace("'>","")

            #subprocess.call(consoleinput)

        if lastcheck!=self.sheetchecker.checkwhenupdated():
            #spreadsheetmust be updated

            csv= self.sheetchecker.getupdatedcsv()
            self.sheetchecker.UpdateURLsonSheet(csv)
            self.sheetchecker.UpdateScreenshotURLsonSheet(csv)
            demopageupdater(csv)
            print "i finished updated the demo pages"
            logging.debug("i finished updated the demo pages"+str(datetime.datetime.now()))
            gitupdate()
            logging.debug("i finished updated the git"+str(datetime.datetime.now()))

def timeoutexception():
    raise

if __name__ == "__main__":

    print 'Starting SheetCheckerthread...'

    SheetChecker = SheetCheckerThread()

    while 1:

        timerout=Timer(600,timeoutexception)
        timerout.start()

        try:
            SheetChecker.checksheet()
        except Exception:

            logging.debug(str(traceback.format_exc()))
            logging.debug("exception in main try occured")
            SheetChecker = SheetCheckerThread()
            print "sheetchecker broke"


        timerout.cancel()

print 'Exiting'


