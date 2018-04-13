# creates and applies the S3 bucket webconfig redirect

import boto3

s3 = boto3.client('s3')

# create website configuration
website_configuration = {
    'RedirectAllRequestsTo': {
        'HostName': 'second-to-none.com',
        'Protocol': 'http',
    },
}

# apply the policy to the bucket
with open('testbucketlist.txt') as in_file:
    for bucket_name in in_file:
        bucket = bucket_name.replace('\n', '')
	print("Pushing webconfig for bucket: {}".format(bucket))
	s3.put_bucket_website(
    	    Bucket=bucket,
    	    WebsiteConfiguration=website_configuration
	)


