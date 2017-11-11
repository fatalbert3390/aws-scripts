# script designed to utilize boto3 commands to create an s3 bucket
# by reading a list of domains and piping each line into the "create bucket"
# command and creating each bucket individually

import boto3

s3 = boto3.client('s3')
l = open('testbucketlist.txt')

s3.create_bucket(Bucket='%' % l.readline())
