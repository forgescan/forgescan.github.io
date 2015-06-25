#v2. Makes the demopages
from HAPYAKFUNCTIONS import *
import os
import s3interface
import logging
import ConfigParser
import io

###accesses config file
demomaker_config=(open("demomaker.cfg","r").read())
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(demomaker_config))

###starterrorlogging
logging.basicConfig(filename=config.get("config","pathtoerrorlog"),level=logging.DEBUG)

#initiates stuff
S3session=s3interface.S3session()
#print S3session.uploadfile("templatehtml.html")

#create GUID for each firm
#so check if sheet is updated
sheetchecker=GoogleDocsSessionv2()

print sheetchecker.checkwhenupdated()
#for i in range(10):
#    sheet=sheetchecker.currentworksheet.get_all_records()
#    print len(sheet)
sheet=sheetchecker.currentworksheet.get_all_records()
print sheet[0]






"""
while 1:

    try:
        #checks for change to the spreadsheet
        #if change occurs //

    except:
        error="s3 uploadfailed"+str(traceback.format_exc())
        logging.error(error)
        print error
        return -1
        #logs error to log and restarts
"""