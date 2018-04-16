# starts instance specified by instance ID

import boto3

ec2 = boto3.client('ec2')

ec2.start_instances(
    InstanceIds=[
        'i-########',
    ]
)
