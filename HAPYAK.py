#!/usr/bin/python

import os
import logging
logging.basicConfig(filename='testlog.log',level=logging.DEBUG)
import traceback
logging.debug("filestarted imported")

import time
cwd=os.getcwd()
os.mkdir(cwd+"/testdir")

while True:
    logging.debug("here im logingincrap")
    time.sleep(1)
    pass

