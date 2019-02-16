# Adds an instance to a load balancer
# 
# This script is intended to be run on a failed
# load balancer health check/CW alarm

import boto3

elb = boto3.client('elb')

def lambda_handler(event, context):
    elb.register_instances_with_load_balancer(
            LoadBalancerName='[ELB NAME]',
            Instances=[
                {
                    'InstanceId': 'i-########'
                },
           ]
    )
