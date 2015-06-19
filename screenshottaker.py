import os
import urllib
import system
##screenshottaker001
try:
    cwd=os.getcwd()
    #print os.listdir(cwd+'/web')
    firmlist=os.listdir(cwd+'/web')
    #print firmlist
    print len(firmlist)
    for firm in firmlist:
        try:
            print firm
            print cwd+'/web/'+str(firm)
            LandingPageURL="http://forgescan.github.io/web/"+urllib.quote()+"/"+urllib.quote(firm[0])+".html"
            firmfolder =os.listdir(cwd+'//web//'+str(firm))
            ##gonna update all firms for now
            
        except:pass
except:pass
