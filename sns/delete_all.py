# Deletes all SNS topics and subscriptions within the region specified in your AWS credentials file

import boto3
import json

snsc = boto3.client('sns')
snsr = boto3.resource('sns')
marker = None

print("Deleting SNS Topics...")
while True:
    paginator = snsc.get_paginator('list_topics')
    topic_iterator = paginator.paginate(
        PaginationConfig={'StartingToken': marker}
    )
    for page in topic_iterator:
        topiclist = page['Topics']
        for topic in topiclist:
            topicarn = topic['TopicArn']
            print(topicarn)            
            snsr.Topic(arn=topicarn).delete()
    try:
        marker = page['NextToken']
    except KeyError:
        break

print("Deleting SNS Subscriptions...")
while True:
    paginator = snsc.get_paginator('list_subscriptions')
    topic_iterator = paginator.paginate(
        PaginationConfig={'StartingToken': marker}
    )
    for page in topic_iterator:
        sublist = page['Subscriptions']
        for sub in sublist:
            subarn = sub['SubscriptionArn']
            print(subarn)            
            snsr.Subscription(arn=subarn).delete()
    try:
        marker = page['NextToken']
    except KeyError:
        break
