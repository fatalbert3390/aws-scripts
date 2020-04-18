# deletes log groups

import boto3
import json
from pprint import pprint

client = boto3.client('logs')

result = client.describe_log_groups()
# print(result)
# pprint(result)
llist= []

for log in result['logGroups']:
    llist.append(log['logGroupName'])

for group in llist:
    client.delete_log_group(logGroupName=group)
    print("Deleting log group: {}".format(group))