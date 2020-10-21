# Deletes all lambda functions within the region specified in your AWS credentials file

import boto3
import json

client = boto3.client('lambda')
result = client.list_functions()
marker = None

print("Deleting Lambda Functions...")
while True:
    paginator = client.get_paginator('list_functions')
    topic_iterator = paginator.paginate(
        PaginationConfig={'StartingToken': marker}
    )
    for page in topic_iterator:
        llist = page['Functions']
        for func in llist:
            func_name = func['FunctionName']
            print(func_name)            
            client.delete_function(FunctionName=func_name)
    try:
        marker = page['NextToken']
    except KeyError:
        break