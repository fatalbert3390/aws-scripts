# stops instance specified by instance ID
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    ec2.stop_instances(
        InstanceIds=[
            'i-########',
        ]
    )
