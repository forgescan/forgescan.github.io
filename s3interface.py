from boto.s3.connection import S3Connection
awskeystore=open("/root/home/ubuntu/rootkey.csv","r")
awskeystore=awskeystore.read()
print awskeystore
conn = S3Connection(AWS_KEY, AWS_SECRET)
bucket = conn.get_bucket(BUCKET)
destination = bucket.new_key()
destination.name = filename
destination.set_contents_from_file(myfile)
destination.make_public()