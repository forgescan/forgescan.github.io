#!/usr/bin/python
# -*- coding: cp1252 -*-
import json
import gspread
import os
from oauth2client.client import SignedJwtAssertionCredentials
import urllib
import traceback
import logging



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
"""            
        
session=GoogleDocsSession()
csv=session.getupdatedcsv()
session.UpdateURLsonSheet(csv)

cell_list = session.currentworksheet.range('Q1:Q'+str(firmlength))
cell_values = urllandingpages

for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
    cell_list[i].value = val    #use the index on cell_list and the val from cell_values

session.currentworksheet.update_cells(cell_list)


#print session.currentworksheet.get_all_values()
#session.currentworksheet.update_cells([12,3,"thing1"])
#csv=GoogleDocsSession().getupdatedcsv()
#print csv

#print GoogleDocsSession().UpdateURLsonSheet(csv)
    

        

        


"""
