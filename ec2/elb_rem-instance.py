# removes an instance from ELB

import boto3

def lambda_handler(event, context):
    elb = boto3.client('elb')
    
    elb.deregister_instances_from_load_balancer(
        LoadBalancerName='[ELB NAME]',
        Instances=[
            {
                'InstanceId': 'i-######'
            },
        ]
    )