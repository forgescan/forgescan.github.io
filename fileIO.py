#csv=open("C:/Users/Derrick/Desktop/hapyaktest002/python program/hapyak002/csv file drop/elearningcsv001.csv","r")
#csv=csv.read()
#print len(csv)
import os
import logging
logging.basicConfig(filename='demomaker.log',level=logging.DEBUG)
import traceback
logging.debug("fileiowas imported")

cwd=os.getcwd()

print cwd

def fileIn(relativeaddress):
    filein=open(str(relativeaddress),"r")
    filein=filein.read()
    return filein


def hapyakfileOut(firm,typeoffile,stringfile):
    companyname=firm[0]
    directorydesired=cwd+"/web/"+companyname
    try:os.mkdir(cwd+"/web")
    except Exception:
        logging.debug(str(traceback.format_exc()))
	logging.debug("fileiowas broke")
    try:os.mkdir(directorydesired)
    except Exception:
        logging.debug(str(traceback.format_exc()))
	logging.debug("fileiowas broke")
    
    fileout=open(directorydesired+"/"+companyname+typeoffile,"w")
    fileout.write(stringfile)
    fileout.close
"""
def hapyakfileOut(filename,stringfile):
    companyname=filename.split(".")[0]
    directorydesired=cwd+"\\web\\"+companyname
    try:os.mkdir(cwd+"\\web")
    except:pass
    try:os.mkdir(directorydesired)
    except:pass
    
    fileout=open(directorydesired+"\\"+filename,"w")
    fileout.write(stringfile)
    fileout.close
"""    
####################bad below
    
    

def fileOut(relativeaddress,stringfile):
    print relativeaddress
    print relativeaddress.split("/")[0]
    directorydesired=cwd+"\\web\\"+relativeaddress.split("\\")[1].split("""/""")[0]
    
    #print cwd+"/"+relativeaddress.split("/")[1]
    #os.mkdir(cwd+"\\"+relativeaddress.split("/")[1].split("""\\""")[0])
    try:os.mkdir(cwd+"\\web")
    except:
        pass
    try:os.mkdir(directorydesired)
        

    except:
        pass
    #clunky way to pull proper directory out of string
    fileout=open(cwd+"\\web"+relativeaddress,"w")
    fileout.write(stringfile)
    fileout.close()
    
 


class Team:
  def __init__(self):
    self.name = None
    self.logo = None
    self.members = 0
