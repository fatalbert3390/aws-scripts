# script for importing a domain list and requesting certificates

import boto3

acm = boto3.client('acm')

with open('testbucketlist.txt') as in_file:
    for bucket_name in in_file:
        bucket = bucket_name.replace('\n', '')
        print("Requesting certificate for site: {}".format(bucket))

acm.request_certificate(
    DomainName=bucket,
    SubjectAlternativeNames=[
	'*.{}'.format(bucket),
    ],
)

