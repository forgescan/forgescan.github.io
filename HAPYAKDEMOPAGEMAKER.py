#v2. Makes the demopages
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
logging.basicConfig(filename=config.get("config","pathtolog"),level=logging.DEBUG)

#initiates stuff
fileuploader=s3interface.S3session
print fileuploader


"""
while 1:
    try:
        #checks for change to the spreadsheet
        #if change occurs //
    except:
        #logs error to log and restarts
"""