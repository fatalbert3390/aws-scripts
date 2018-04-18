import boto3
import re

client = boto3.client("route53")

# json would be your reponse to play with
json = client.list_hosted_zones()

# hosted_zones is just well...your hosted zones
hosted_zones = json['HostedZones']

regexp = re.compile("/hostedzone/(.*)$")

for hosted_zone in hosted_zones:
	print(regexp.search(hosted_zone['Id']).group(1))
