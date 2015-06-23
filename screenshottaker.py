import os
import urllib
import sys
import time
import HAPYAKFUNCTIONS

os.chdir("/home/ubuntu/forgescan.github.io/")
##screenshottaker001


try:
    #os.system("sudo Xvfb :5 -screen 0 720x464x24 & ") #initiate virtual display buffer
    cwd=os.getcwd()
    #print os.listdir(cwd+'/web')
    cwd='/home/ubuntu/forgescan.github.io/'
    firmlist=os.listdir(cwd+'/web')
    csv=open(cwd+"HAPYAKCSV.csv").read()
    csv=csv.replace('"','')
    csv=csv.replace('.','') #eliminates extraneous characters
    firms=csv.split("\n")
    #for testing purposes
    #firms=[firms[1],firms[2],firms[3],firms[4]] #remove later
    #try:
    for i in range(len(firms)-10):
        firm=firms[i]
        try:
            os.system("sudo Xvfb :5 -screen 0 720x464x24 & ") #initiate virtual display buffer
            pass
        except:pass

        firm=firm.split(',')
        #print firm
        if firm[2]!='' and firm[3]!='': #commas in company names screw everything up
            print firm[2]

            EmbeddedVideoURL=HAPYAKFUNCTIONS.URLbuilder(firm)

            firm=firm[0]


            #except:pass
            #print firmlist

            print firm
            print cwd+'/web/'+str(firm)
            LandingPageURL="http://forgescan.github.io/web/"+urllib.quote(firm)+"/"+urllib.quote(firm)+".html"
            print LandingPageURL
            firmfolder =os.listdir(cwd+'//web//'+str(firm))
            #time.sleep(1)
            os.system("sudo DISPLAY=:5 google-chrome --incognito --kiosk --window-size=720,464 --window-position=0,0 '"+EmbeddedVideoURL+ "'&")  #--make-default-browser
            time.sleep(5)
            #delays would be placed here
            os.system("sudo DISPLAY=:5 import -window root '"+cwd+"web/"+firm+"/"+firm+".png'")
            print "sudo DISPLAY=:5 google-chrome  --kiosk --window-size=720,464 --window-position=0,0 '"+EmbeddedVideoURL+ "'&"
            print "sudo DISPLAY=:5 import -window root "+cwd+"web/"+firm+"/"+firm+".png"
            time.sleep(3)

        os.system("sudo killall Xvfb")



        ##gonna update all firms for now
            
        #except:pass
except:pass
