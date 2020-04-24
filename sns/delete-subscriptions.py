# deletes lambda functions (up to 50 at a time)

import boto3
import json
from pprint import pprint

client = boto3.client('sns')

result = client.list_subscriptions()

llist= []

for endpoint in result['Subscriptions']:
    llist.append(endpoint['SubscriptionArn'])

for sub in llist:
    client.unsubscribe(SubscriptionArn=sub)
    print("Deleting Subscription: {}".format(sub))