# This script deletes a bunch of random ass stuff left over from a certain shitty SaaS product
# This is the nuclear option - it deletes everything with prejudice, so be careful

import boto3
import json
 
snsc = boto3.client('sns')
snsr = boto3.resource('sns')
logclient = boto3.client('logs')
lamclient = boto3.client('lambda')
marker = None
 
# ############################
# # Deletes Lambda functions #
# ############################
 
print("\nDeleting Lambda Functions...\n")
while True:
    paginator = lamclient.get_paginator('list_functions')
    topic_iterator = paginator.paginate(
        PaginationConfig={'StartingToken': marker}
    )
    for page in topic_iterator:
        llist = page['Functions']
        for func in llist:
            func_name = func['FunctionName']
            print(func_name)            
            lamclient.delete_function(FunctionName=func_name)
    try:
        marker = page['NextToken']
    except KeyError:
        break

#################################
# Deletes CloudWatch log groups #
#################################

print("\nDeleting CloudWatch log groups...\n")
while True:
    paginator = logclient.get_paginator('describe_log_groups')
    topic_iterator = paginator.paginate(
        PaginationConfig={'StartingToken': marker}
    )
    for page in topic_iterator:
        loglist = page['logGroups']
        for log in loglist:
            log_name = log['logGroupName']
            print(log_name)
            logclient.delete_log_group(logGroupName=log_name)
    try:
        marker = page['NextToken']
    except KeyError:
        break

########################################
# Deletes SNS Topics and Subscriptions #
########################################

# * Within the region specified in your AWS credentials file

print("\nDeleting SNS Topics...\n")
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

print("\nDeleting SNS Subscriptions...\n")
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
