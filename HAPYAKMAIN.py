#!/usr/bin/python
# -*- coding: cp1252 -*-
import os
import logging
import traceback
import threading
from threading import Thread
import subprocess
import datetime
import time
from threading import Timer
from fileIO import *
from HAPYAKFUNCTIONS import *
import gspread002


os.chdir("/home/ubuntu/forgescan.github.io/")#important when running as service cwd is /

logfile=open("/home/ubuntu/forgescan.github.io/demomaker.log","w") #on restart make a new log
logfile.close()

logging.basicConfig(filename='demomaker.log',level=logging.DEBUG)
logging.debug("Logging Started")










class SheetCheckerThread():

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
            os.system("sudo python screenshottaker.py &")#launches screenshottaking process which runs through the HAPYAKCSV.csv
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
            logging.debug("i finished and updated the demo pages"+str(datetime.datetime.now()))
            gitupdate()
            logging.debug("I Pushed to git"+str(datetime.datetime.now()))

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


