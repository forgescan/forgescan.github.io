#!/usr/bin/python
# -*- coding: cp1252 -*-
from fileIO import *
from HAPYAKFUNCTIONS import *

import logging
logging.basicConfig(filename='demomaker.log',level=logging.DEBUG)




def SplitandReplace(keywords,firm, stringfile):
    print keywords
    #print firm
    #print len(stringfile)
    
    #try:
    for index in range(len(keywords)):
        stringfileplaceholder=""
        print keywords[index]
        print len(keywords)
        print "heres the index"+str(index)
        if keywords[index]!=None and firm[index]!="":
            stringfile=stringfile.replace(keywords[index],firm[index])
    return stringfile
"""                                        
print "i started teh stuff"
CSSKEYWORDS=['~COMPANY~',None,None,'~Logo~','~Major Hex~','~Minor Hex~']
css=fileIn("templateCSS/templatecss.css")
csv=csv.split("\n")
firm=csv[2]
#print firm
#print css
firm=firm.split(",")
print firm
"""
from threading import Thread


import threading

theVar = 1
"""
class MyThread ( threading.Thread ):

   def run ( self ):

      global theVar
      print "This is thread" + str ( theVar ) + "speaking."
      print "Hello and good bye."
      theVar = theVar + 1

for x in xrange ( 20 ):
   MyThread().start()
print 'Print this line to be sure we get here after starting the thread loop...'  """
#from gspread001 import *
import gspread002
import time
import sys
from threading import Timer
from multiprocessing import Process
  

class googledocschecker ( threading.Thread ):
    lasttime=""
    def run (self):
        while 1:  
            try:
                updatecheck=checkwhenupdated()
                print updatecheck
                if updatecheck!=googledocschecker.lasttime:
                  print "i think i got updated"+googledocschecker.lasttime
                  googledocschecker.lasttime=updatecheck
                  
                  csv=getupdatedcsv()
                  #print csv
                  demopageupdater(csv)
                  #gitupdate()
                  #googledocschecker.lasttime=checkwhenupdated()
                  updatecell(12,"thing")
                  print "i finished updating"

            except Exception, err:
                sys.stderr.write('ERROR: %s\n' % str(err))
                #return 1
                #should restart the login
                #from gspread001 import *
                print "I broke"

#p = Process(target=f, args=('bob',))
#sheetchecker=gspread002.GoogleDocsSession()
sheetchecker=gspread002.GoogleDocsSession


"""
while 1:
    timerout=Timer(5, timeout)
    timerout.start()
    csv= sheetchecker.getupdatedcsv()
    sheetchecker.updatecell("d12","otherthing")
    
    print len(csv)
    print sheetchecker.checkwhenupdated()
    timerout.cancel()
"""

import threading

import ctypes

import time
import traceback


#w32 = ctypes.windll.kernel32

THREAD_TERMINATE = 1 # Privilege level for termination
import datetime
def timeout():
    #global sheetchecker
    
    global SheetChecker
    SheetChecker.kill_thread(SheetChecker) #should kill the thread when it locks up
    
    SheetChecker = SheetCheckerThread()
    SheetChecker.start()
    print "Threadrestarteddue to error"
    
    #raise RuntimeError('this is the error message')#TimeExceededError, "Timed Out"
    logging.debug("timeout, new thread made"+str(datetime.datetime.now()))
    
import subprocess
class SheetCheckerThread(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)

        self.setDaemon(1)
        self.sheetchecker=gspread002.GoogleDocsSession()
        print self.sheetchecker.checkwhenupdated()

    def run(self):

        #self.tid = w32.GetCurrentThreadId()

        while 1:
            try:
                timerout=Timer(60, timeout)
                timerout.start()

                
                
                lastcheck=self.sheetchecker.lastworksheetupdate
                self.sheetchecker.updatecell("U2",str(lastcheck))
                consoleinput=str(self.sheetchecker.currentworksheet.acell("v2"))
                if consoleinput!="<Cell R2C22 ''>":
                    self.sheetchecker.updatecell("V2",str("Command Recieved"))
                
                print consoleinput
                if "~UPDATE~" in consoleinput:
                    subprocess.call("git pull")
                if "~CMD~" in consoleinput:
                    consoleinput=consoleinput.replace("~CMD~","")
                    consoleinput=consoleinput.replace("<Cell R2C22 '","")
                    consoleinput=consoleinput.replace("'>","")
                                      
                    subprocess.call(consoleinput)
                
                if lastcheck!=self.sheetchecker.checkwhenupdated():
                    #spreadsheetmust be updated
                    csv= self.sheetchecker.getupdatedcsv()
                    demopageupdater(csv)
                    gitupdate()
                    self.sheetchecker.UpdateURLsonSheet(csv)
                    

                    #sheet must have been updated recently
                    
                print len(csv)
                print self.sheetchecker.checkwhenupdated()
                timerout.cancel()
		raise 
            except Exception:
                print(traceback.format_exc())
                print "exception happened"
                timeout()
            
            
            
            

    def kill_thread(self,threadobj):
	pass

        #handle = w32.OpenThread(THREAD_TERMINATE, False, threadobj.tid)

        #result = w32.TerminateThread(handle, 0)

        #w32.CloseHandle(handle)
        #print "threadkilled"

        #return result

if __name__ == "__main__":

    print 'Starting SheetCheckerthread...'

    SheetChecker = SheetCheckerThread()

    SheetChecker.start()

    #time.sleep(5)

    #print 'Terminating thread...'

    #x.kill_thread(x)

    #print "threadshouldbedead"
    
    #time.sleep(5)
    while 1:
        pass

print 'Exiting'


