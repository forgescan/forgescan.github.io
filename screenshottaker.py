import os
import urllib
import sys
##screenshottaker001
try:
    sys.call("sudo Xvfb :5 -screen 0 720x464x24 & ") #initiate virtual display buffer
    cwd=os.getcwd()
    #print os.listdir(cwd+'/web')
    firmlist=os.listdir(cwd+'/web')
    #print firmlist
    print len(firmlist)
    for firm in firmlist:
        try:
            print firm
            print cwd+'/web/'+str(firm)
            LandingPageURL="http://forgescan.github.io/web/"+urllib.quote(firm)+"/"+urllib.quote(firm[0])+".html"
            firmfolder =os.listdir(cwd+'//web//'+str(firm))

            sys.call("sudo DISPLAY=:5 google-chrome --kiosk --window-size=720,464 --window-position=0,0 "+LandingPageURL+ "&")
            #delays would be placed here
            sys.call("sudo DISPLAY=:5 import -window root "+cwd+"/web/"+firm+"/"+firm+".png")



            ##gonna update all firms for now
            
        except:pass
except:pass
