#v2. Makes the demopages
from HAPYAKFUNCTIONS import *
import os
import s3interface
import logging
import ConfigParser
import io
import uuid

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
def return1(firm):
    return firm["Website"]
    #return "one"
worksheet=sheetchecker.currentworksheet
def iterateandreplace(keyword, function, worksheet):
    try:
        column=str(sheetchecker.currentworksheet.find(keyword)).split("R1C")[1].split(' ')[0]
        print column
        if column=="":
            raise
        column=int(column)
        columnletter=worksheet.get_addr_int(1,column )[0]
        firmlength=len(sheetdict)
        print columnletter
        cell_list = sheetchecker.currentworksheet.range(columnletter+"2:"+columnletter+str(firmlength-1))

        #cell_list=[]
        value_list=[]
        firmcount=0
        for firm in sheetdict:

            try:
                firmcount+=1
                value_list.append(function(firm))
                pass
                #addoutput to list
            except:
                firmcount+=1
                value_list.append("")
                error="iterate and replace failed "+str(traceback.format_exc())
                logging.error(error)
                print error
                pass
                #addfailedtolist
                #errorlogging
            #cell_list+="<Cell R"+str(firmcount)+"C"+str(column)+" '"+str(value)+"'>"
        for i in range(0,len(sheetdict)-10):  #gives us a tuple of an index and value
            cell_list[i].value = value_list[i]    #use the index on cell_list and the val from cell_values
        #del cell_list[0]

        worksheet.update_cells(cell_list)
        #export list to desired column of sheet
    except:
        error="iterate and replace failed "+str(traceback.format_exc())
        logging.error(error)
        print error
        return -1
    print cell_list
    print value_list
def firmdicttolist(firm):# for backwards compatibility with previous code
    keylist=['Company','Website','Video','Logo','Major Hex','Minor Hex','First #1','Last #1','Email #1','First #2','Last #2','Email #2','First #3','Last #3','Email #3','TEMPLATE','LandingPageURLs','ScreenShot URLs','GUID','T']#,'Last Time Updated'
    firmlistout=[]

    for key in keylist:
        firmlistout.append(key)

    return firmlistout

def cssmakerv2(firm):
    firm2=firmdicttolist(firm)

    #print firm2



    locationoftemplateCSS="templateCSS/templatecss.css"
    templatecss=fileIn(locationoftemplateCSS)

    CSSKEYWORDS=['~COMPANY~',None,None,'~Logo~','~Major Hex~','~Minor Hex~']
    updatedtemplate=SplitandReplace(CSSKEYWORDS,firm,templatecss)
    #hex to rgba
    updatedtemplate=updatedtemplate.replace("~majorhextoRGBA~",majorhextoRGBA(firm))
    updatedtemplate=updatedtemplate.replace("~minorhextoRGBA~",minorhextoRGBA(firm))
    #any other replaces can be added here
    fileout=open("/web/"+firm["GUID"]+".css", "w")
    fileout.write(updatedtemplate)
    fileout.close()

    hapyakfileOut(firm,".css",updatedtemplate)

sheetchecker.iteratethroughfirms(cssmakerv2)

#sheetchecker.iterateandreplace("GUID",return1)


    #return "1"
    #return uuid.uuid5(uuid.UUID(),firm["Company"]).hex
#print makeGUID(sheetdict[0]["Company"])
sheetchecker.iterateandreplace("GUID",makeGUID)
#print str(uuid.uuid5(uuid.uuid1(),sheetdict[0]["Company"]).hex)
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