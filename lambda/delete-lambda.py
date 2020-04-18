# deletes lambda functions (up to 50 at a time)

import boto3
import json

client = boto3.client('lambda')

result = client.list_functions()

llist= []

for function in result['Functions']:
    llist.append(function['FunctionName']

for name in llist:
   client.delete_function(FunctionName=name)
   print("Deleting Function: {}".format(name))