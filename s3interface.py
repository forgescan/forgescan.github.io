from boto.s3.connection import S3Connection
awskeystore=open("/home/ubuntu/rootkey.csv","r")
awskeystore=awskeystore.read()
awskeystore=awskeystore.split("""\n""")
AWS_KEY=awskeystore[0].split("=")[1]
AWS_SECRET=awskeystore[1].split("=")[1]

print awskeystore
conn = S3Connection(AWS_KEY, AWS_SECRET)
BUCKET="hapyakdemopagedrop"

bucket = conn.get_bucket(BUCKET)
destination = bucket.new_key()
destination.name = filename
destination.set_contents_from_file(myfile)
destination.make_public()