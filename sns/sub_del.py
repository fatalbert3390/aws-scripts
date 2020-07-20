import boto3
import json

sns = boto3.client('sns')
snsr = boto3.resource('sns')
marker = None

print("Deleting SNS Subscriptions....")
while True:
    paginator = sns.get_paginator('list_subscriptions')
    topic_iterator = paginator.paginate(
        PaginationConfig={'StartingToken': marker}
    )
    for page in topic_iterator:
        snslist = page['Subscriptions']
        for sub in snslist:
            subarn = sub['SubscriptionArn']
            print(subarn)            
            snsr.Subscription(arn=subarn).delete()
    try:
        marker = page['NextToken']
    except KeyError:
        break
