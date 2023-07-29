def local(infile, outfile):
 outfile.write(infile.read())
 outfile.close()
 infile.close()

# ... previous function ommited
def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)
