from boto.s3.connection import S3Connection
awskeystore=open("/home/ubuntu/rootkey.csv","r")
awskeystore=awskeystore.read()
awskeystore=awskeystore.replace('''\r''',"").split("""\n""")
AWS_KEY=awskeystore[0].split("=")[1]
AWS_SECRET=awskeystore[1].split("=")[1]

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
