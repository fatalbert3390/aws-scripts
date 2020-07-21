import boto3
from pprint import pprint

s3 = boto3.client('s3')

bucket_names = []

bucket_list = s3.list_buckets()

for buckets in bucket_list['Buckets']:
    bucket_names.append(buckets['Name'])
    for bucket in bucket_names:
        s3.delete_bucket(Bucket=bucket)
        print("Deleting bucket {}".format(bucket))
