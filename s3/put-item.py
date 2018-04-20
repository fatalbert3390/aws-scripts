import boto3
import time

client = boto3.client('s3')
timestamp = time.strftime("%Y-%m-%d @ %H:%M:%S")

client.put_object(Body=b'test', Bucket='alex-stn-testing', Key='filename ' + timestamp)
