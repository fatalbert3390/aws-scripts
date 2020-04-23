# deletes lambda functions (up to 50 at a time)

import boto3
import json

client = boto3.client('sns')

result = client.list_topics()

llist= []

for topic in result['Topics']:
    llist.append(topic['TopicArn'])

for topicArn in llist:
   client.delete_topic(TopicArn=topicArn)
   print("Deleting Function: {}".format(name))