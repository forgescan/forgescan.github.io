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
sheetdict=sheetchecker.currentworksheet.get_all_records()

print sheetdict[0]["Website"]
def return1():
    return "one"
worksheet=sheetchecker.currentworksheet
def iterateandreplace(keyword, function, worksheet):
    try:
        column=str(sheetchecker.currentworksheet.find(keyword)).split("R1C")[1].split(' ')[0]
        print column
        if column=="":
            raise

        cell_list=[]
        value_list=[]
        firmcount=0
        for firm in sheetdict:
            if firmcount==0:
                firmcount+=1
                continue


            try:
                firmcount+=1
                value=function(firm)
                pass
                #addoutput to list
            except:
                firmcount+=1
                value=None
                pass
                #addfailedtolist
                #errorlogging
            cell_list+="<Cell R"+str(firmcount)+"C"+str(column)+" '"+str(value)+"'>"
        worksheet.update_cells(cell_list)
        #export list to desired column of sheet
    except:
        error="iterate and replace failed "+str(traceback.format_exc())
        logging.error(error)
        print error
        return -1

iterateandreplace("GUID",return1,worksheet)
"""
cell_list = sheetchecker.currentworksheet.range('T3:T10')
#print cell_list
print sheetchecker.currentworksheet.find("GUID")
cell_values = [2321,4324,6564,2434]#self.urllandingpages
try:
    for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
        cell_list[i].value = val    #use the index on cell_list and the val from cell_values
except: pass#Exception:print(traceback.format_exc())
print cell_list

sheetchecker.currentworksheet.update_cells(cell_list)
"""

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