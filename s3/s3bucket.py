# creates s3 buckets from a list and pushes a simple web config to them

import boto3

s3 = boto3.client('s3')

web_config = {
    'RedirectAllRequestsTo': {
	'HostName': 'domain.com',
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
        )
