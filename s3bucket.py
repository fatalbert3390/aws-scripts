# script designed to utilize boto3 commands to create an s3 bucket
# and push a simple web config to it
# by reading a list of domains and piping each line into the "create bucket"

import boto3

s3 = boto3.client('s3')

web_config = {
    'RedirectAllRequestsTo': {
	'HostName': 'second-to-none.com',
	'Protocol': 'http',
    },
}

with open('testbucketlist.txt') as in_file:
    for bucket_name in in_file:
        bucket = bucket_name.replace('\n', '')
        print("Creating: {}".format(bucket))
        s3.create_bucket(Bucket=bucket)
        s3.put_bucket_website(
            Bucket=bucket,
            WebsiteConfiguration=web_config
