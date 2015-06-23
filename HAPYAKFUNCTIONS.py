from fileIO import *
import urllib, urllib2, cookielib
import traceback
import gspread002
import logging
import time
import json
import gspread
import os
from oauth2client.client import SignedJwtAssertionCredentials
import logging





specialcommands=[""]
#'~COMPANY~',None,None,'~Logo~','~Major Hex~','~Minor Hex~'

#keywordsfunctions 
def majorhextoRGBA(firm):
    try:
        hexin=firm[4].replace("#","")  #prescreening to pull hashtag out 
        Rint=int(hexin[0:2],16)
        Gint=int(hexin[2:4],16)
        Bint=int(hexin[4:6],16)
        Afloat=.8
        return str(Rint)+", "+str(Gint)+", "+str(Bint)+", "+str(Afloat)
    except: #so if for any reason it fails this heres where the default majorhex value goes
        return "26, 117, 207, .5"

def minorhextoRGBA(firm):
    try:
        hexin=firm[5].replace("#","")
        Rint=int(hexin[0:2],16)
        Gint=int(hexin[2:4],16)
        Bint=int(hexin[4:6],16)
        Afloat=.8
        return str(Rint)+", "+str(Gint)+", "+str(Bint)+", "+str(Afloat)
    except: #so if for any reason it fails this heres where the default minorhex value goes
        return "26, 117, 207, .5"
def URLbuilder(firm):
    #URLtemplate="""http://www.hapyak.com/?embed=true&edit=false&startInEditMode=false&track=137995&project=19052&key=7f4e59105b08445b9394&source=youtube&source_id=8KZ8m4cpnyk&css=http%3A%2F%2Fforgescan.github.io%2Fstylesheets%2Fmicro2.css&external=true&reset_variables=true&is_template=false&autoplay=true&captions=false&hapyak_username=walmart&companyName=walmartinc"""

    try:URLCOMPANY=urllib.quote(firm[0])
    except:URLCOMPANY="default"
    try:URLUSERID=urllib.quote(firm[6])
    except:URLUSERID="default"
    try:URLCSS="http://forgescan.github.io/web/"+firm[0]+"/"+firm[0]+".css"
    except: URLCSS="http://forgescan.github.io/web/Exxon%20Mobil/Exxon%20Mobil.css"  #place default css here
    URLCSS=urllib.quote(URLCSS)
    try:URLVIDEO=firm[2].split("=")[-1]
    except:URLVIDEO="8KZ8m4cpnyk"
    try:URLTRACK="137995" #firm[9]  #need to set the tracks equal to somthingneed to set 
    except:URLTRACK="137995" #default track
    try:URLPROJECT="19052"
    except:URLPROJECT="19052"
    #simplify and expand later
    
    URLtemplate="""http://www.hapyak.com/?embed=true&edit=false&startInEditMode=false&track="""+URLTRACK+"""&project="""+URLPROJECT+"""&key=7f4e59105b08445b9394&source=youtube&source_id="""+URLVIDEO+"""&css="""+URLCSS+"""&external=true&reset_variables=true&is_template=false&autoplay=false&captions=false&hapyak_username="""+URLUSERID+"""&companyName="""+URLCOMPANY

    return URLtemplate

def SplitandReplace(keywords,firm, stringfile):

    for index in range(len(keywords)):
        if keywords[index]!=None and firm[index]!="":
            stringfile=stringfile.replace(keywords[index],firm[index])
    return stringfile

#['Company', 'Website', 'Video', 'Logo', 'Major Hex', 'Minor Hex', 'First #1', 'Last #1', 'Email #1', 'First #2', 'Last #2', 'Email #2', 'First #3', 'Last #3', 'Email #3', 'Landing Page URL', '"']

def cssmaker(firm):
    
    locationoftemplateCSS="templateCSS/templatecss.css"
    templatecss=fileIn(locationoftemplateCSS)
    
    CSSKEYWORDS=['~COMPANY~',None,None,'~Logo~','~Major Hex~','~Minor Hex~']
    updatedtemplate=SplitandReplace(CSSKEYWORDS,firm,templatecss)
    #hex to rgba
    updatedtemplate=updatedtemplate.replace("~majorhextoRGBA~",majorhextoRGBA(firm))
    updatedtemplate=updatedtemplate.replace("~minorhextoRGBA~",minorhextoRGBA(firm))
    #any other replaces can be added here

    hapyakfileOut(firm,".css",updatedtemplate)
    #log could be returned here if wanted



    
def htmlmaker(firm):
    locationoftemplateHTML="templateHTML/templatehtml.html"
    templatehtml=fileIn(locationoftemplateHTML)
    HTMLKEYWORDS=['~COMPANY~',None,None,'~Logo~','~Major Hex~','~Minor Hex~']
    updatedtemplate=SplitandReplace(HTMLKEYWORDS,firm,templatehtml)
    updatedtemplate=updatedtemplate.replace("~URL~",URLbuilder(firm))
    #~URL~ is our keyword
    
    hapyakfileOut(firm,".html",updatedtemplate)
    
def findlogo(firm):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.open("http://"+firm[1])#, login_data)
    resp = opener.open("http://"+firm[1])
    htmlfrompage=resp.read()
    
   
    htmlfrompage=htmlfrompage.split("\n")
    for line in htmlfrompage:
        if "logo" in line:
            #print "theres a logo"
            #print line+"\n"
            line=line.split('"')
            for part in line:
                if "logo" in part:
                    #print part
                    if "." in part:
                        #this gets the logo
                        if part[0]=="/":
                            return "http://"+firm[1]+part
                            
                        return part
def demopageupdater(csv):
    try:
        csv=csv.split('"')
        csv="".join(csv)


        firms=csv.split("\n")
        firmlist=[]
        for firm in firms:
            firm=firm.replace('"',"") #get rid of unwanted characters here
            firm=firm.replace(".","")
            firmlist.append(firm.split(","))

        updatedfirmlist=[]
        logolist=[]
        firmcount=0
        for firm in firmlist:

            
            if len(firm)<2:
                continue
            #print firm
            try:cssmaker(firm)
            except:pass
            try:htmlmaker(firm)
            except:
                print "I failed to makehtml on firm "+firm[0]
                pass

    except Exception:
        logging.debug(str(traceback.format_exc()))
        print(traceback.format_exc())

def gitupdate():
    import subprocess
    kwargs = {}
    if subprocess.mswindows:
        su = subprocess.STARTUPINFO()
        su.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        su.wShowWindow = subprocess.SW_HIDE
        kwargs['startupinfo'] = su
    try:
        p = subprocess.Popen(['pwd'],shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,**kwargs)
        out, err = p.communicate()
        print out
        logging.debug("heres the CWD"+str(out))


        #os.system("git add .")
        p = subprocess.Popen(['git add .'],shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,**kwargs)
        out, err = p.communicate()
        print out
        logging.debug(str(out))


        #os.system("git commit -a -m hapyak")

        p = subprocess.Popen(['git commit -a -m hapyak'],shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,**kwargs)
        out, err = p.communicate()
        print out
        logging.debug(str(out))
        logging.debug(str(err))
        #logging.debug(str(traceback.format_exc()))

        #os.system("git push -f")
        os.system("git push -f")
        time.sleep(2)
        p = subprocess.Popen(['su - ubuntu -c "cd forgescan.github.io; pwd; git push"'],shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,**kwargs)
        out, err = p.communicate()
        print out
        logging.debug(str(out))
        logging.debug(str(err))

        logging.debug("got to end of git stuff")


    except Exception:
        logging.debug("git fail"+str(traceback.format_exc()))
        print(traceback.format_exc())
        print "failedtoupdate"


class GoogleDocsSession():

    """Handles the connection with the googleDocs API uses Gspread
    """

    def __init__(self):
        import json
        import gspread
        import os
        from oauth2client.client import SignedJwtAssertionCredentials

        self.cwd=os.getcwd()
        #self.json_key=json.load(open('C:/hapyakdemomaker-3bd41eed62f1.json'))#change path to whereever key is stored
        self.json_key=json.load(open('/home/ubuntu/hapyakdemomaker-3bd41eed62f1.json'))#change path to whereever key is stored
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.client_email="205443885400-cdl80r1q3am00nv1tnont4i2urafla3j@developer.gserviceaccount.com"
        self.credentials = SignedJwtAssertionCredentials(self.json_key['client_email'], self.json_key['private_key'], self.scope)
        self.headers = gspread.httpsession.HTTPSession(headers={'Connection':'Keep-Alive','Timeout':"1"})
        self.session= gspread.authorize(self.credentials)
        self.worksheet1 = self.session.open("Copy of Template Videos").sheet1
        self.currentworksheet=self.session.open("Copy of Template Videos").sheet1
        self.lastworksheetupdate=""
        self.currentcsv=""

    def login(self):
        self.session= gspread.authorize(self.credentials)
    def getupdatedcsv(self):
        logging.debug("geting updated csv")

        self.login()
        self.loadworksheet()
        self.currentcsv=self.currentworksheet.export(format='csv').read()
        ###### save csv locally
        cwd='/home/ubuntu/forgescan.github.io/'
        fileout=open(cwd+"HAPYAKCSV.csv","w")
        fileout.write(self.currentcsv)
        fileout.close()

        return self.currentcsv
    def loadworksheet(self):#,currentworksheet):
        logging.debug("loadingworksheet")
        self.currentworksheet=self.session.open("Copy of Template Videos").sheet1  #lazy cludge fix later
        #return self.session.open(self.current
    def updatecell(self,cell,string):
        self.login()
        self.loadworksheet()
        self.currentworksheet.update_acell(cell,string)#requires cell as string "A5"
    def checkwhenupdated(self):
        logging.debug("checkwhenupdated")
        self.login()
        self.loadworksheet()
        updatedtime=self.currentworksheet.updated
        self.lastworksheetupdate=updatedtime
        return self.lastworksheetupdate
    def UpdateURLsonSheet(self,csv):
        logging.debug("updating urls on sheet")
        firms=csv.split("\n")
        firmcount=1  #-1
        self.firmlength=len(firms) #so it doesnt keep adding forever
        print self.firmlength
        self.urllandingpages=[]

        for firm in firms:
            firmcount+=1
            try:
                firm=firm.replace('"',"") #get rid of unwanted characters here
                firm=firm.replace(".","")
                firm=firm.split(",")
                if len(firm)>2 and firmcount>0:
                    #print firm
                    LandingPageURL="http://forgescan.github.io/web/"+urllib.quote(firm[0])+"/"+urllib.quote(firm[0])+".html"
                    self.urllandingpages.append(str(LandingPageURL))
                    #self.updatecell("Q"+str(firmcount),str(LandingPageURL))
                    #print LandingPageURL
            except Exception:print(traceback.format_exc())
        try:
            del self.urllandingpages[0]
            cell_list = self.currentworksheet.range('Q2:Q'+str(self.firmlength-10))
            #print cell_list
            cell_values = self.urllandingpages
            try:
                for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
                    cell_list[i].value = val    #use the index on cell_list and the val from cell_values
            except: pass#Exception:print(traceback.format_exc())
            self.currentworksheet.update_cells(cell_list)
        except Exception:
            logging.debug(str(traceback.format_exc()))
            print(traceback.format_exc())

    def UpdateScreenshotURLsonSheet(self,csv):
        logging.debug("updating urls on sheet")
        firms=csv.split("\n")
        firmcount=1  #-1
        self.firmlength=len(firms) #so it doesnt keep adding forever
        print self.firmlength
        self.urllandingpages=[]

        for firm in firms:
            firmcount+=1
            try:
                firm=firm.replace('"',"") #get rid of unwanted characters here
                firm=firm.replace(".","")
                firm=firm.split(",")
                if len(firm)>2 and firmcount>1:
                    #print firm
                    LandingPageURL="http://forgescan.github.io/web/"+urllib.quote(firm[0])+"/"+urllib.quote(firm[0])+".png"
                    self.urllandingpages.append(str(LandingPageURL))
                    #self.updatecell("Q"+str(firmcount),str(LandingPageURL))
                    #print LandingPageURL
            except Exception:print(traceback.format_exc())

        try:
            del self.urllandingpages[0]
            cell_list = self.currentworksheet.range('R2:R'+str(self.firmlength-10))#was q1
            #print cell_list
            cell_values = self.urllandingpages
            try:
                for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
                    cell_list[i].value = val    #use the index on cell_list and the val from cell_values
            except: pass#Exception:print(traceback.format_exc())
            self.currentworksheet.update_cells(cell_list)
        except Exception:
            logging.debug(str(traceback.format_exc()))
            print(traceback.format_exc())

    

