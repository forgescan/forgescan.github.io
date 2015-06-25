

import ConfigParser
import io

###accesses config file
demomaker_config=(open("demomaker.cfg","r").read())
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(demomaker_config))


#produces AWS_KEY and Secret
awskeystore=open(config.get("config","pathtoS3key"),"r")
awskeystore=awskeystore.read()
awskeystore=awskeystore.replace('''\r''',"").split("""\n""")
AWS_KEY=awskeystore[0].split("=")[1]
AWS_SECRET=awskeystore[1].split("=")[1]

class S3session():

    """Handles the connection with the S3 api uses Boto
    """
    def __init__(self):
        from boto.s3.connection import S3Connection
        awskeystore=open(config.get("config","pathtoS3key"),"r")
        awskeystore=awskeystore.read()
        awskeystore=awskeystore.replace('''\r''',"").split("""\n""")
        self.AWS_KEY=awskeystore[0].split("=")[1]
        self.AWS_SECRET=awskeystore[1].split("=")[1]
        #initiates connection
        self.S3conn=S3Connection(self.AWS_KEY,self.AWS_SECRET)
        #self.currentbucketname=(config.get("config","defaultbucket"))
        self.Bucket=S3conn.get_bucket(config.get("config","defaultbucket"))




    def listallbuckets(self):
        return S3conn.get_all_buckets()

    def uploadtoS3(self,filename):#specifically for demomaker, uploads to page folder corresponding to the file type
        localfiledump=config.get("config","pathtolocalfiledump")
        filetype=filename.split(".")[-1]
        directory="unknown"
        if filetype==".png":
            directory="media"
        if filetype==".html":
            directory="html"
        if filetype==".css":
            directory="css"
        filetobeuploaded=open(localfiledump+filename,"r")
        destination=bucket.new_key(filename)
        destination.name=directory+"/"+filename
        destination.set_contents_from_file(filetobeuploaded)
        destination.make_public()







print awskeystore
conn = S3Connection(AWS_KEY, AWS_SECRET)
print conn.get_all_buckets()

BUCKET="hapyakdemopagedrop"

myhtml=open("/home/ubuntu/forgescan.github.io/templateHTML/templatehtml.html")

bucket = conn.get_bucket(BUCKET)
destination = bucket.new_key("something.html")
destination.name = "PNGs/something.html"
destination.set_contents_from_file(myhtml)
destination.make_public()
