# script designed to utilize boto3 commands to create an s3 bucket
# by reading a list of domains and piping each line into the "create bucket"
# command and creating each bucket individually

import boto3

s3 = boto3.client('s3')

with open('testbucketlist.txt') as in_file:
    for bucket_name in in_file:
        bucket = bucket_name.replace('\n', '')
        print("Creating: {}".format(bucket))
        s3.create_bucket(Bucket=bucket)

# create website configuration
website_configuration = {
    'RedirectAllRequestsTo': {
	'HostName': 'second-to-none.com',
	'Protocol': 'http',
    },
}

# apply the policy to the bucket
s3.put_bucket_website(
    Bucket=bucket,
    WebsiteConfiguration=website_configuration
)
