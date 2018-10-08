# adds an instance to the 'ELB' load balancer

import boto3

elb = boto3.client('elb')

def lambda_handler(event, context):
    elb.register_instances_with_load_balancer(
            LoadBalancerName='elb',
            Instances=[
                {
                    'InstanceId': 'i-043fb34130a892840'
                },
           ]
    )