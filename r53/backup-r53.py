import boto3
import re

r53_client = boto3.client('route53')
s3_client = boto3.client('s3')
# json would be your reponse to play with
json = r53_client.list_hosted_zones()

# hosted_zones is just well...your hosted zones
hosted_zones = json['HostedZones']

regexp = re.compile("/hostedzone/(.*)$")

for hosted_zone in hosted_zones:
    zone_id = regexp.search(hosted_zone['Id']).group(1)
    print r53_client.list_resource_record_sets(HostedZoneId=zone_id)

s3_client.put_object(Bucket='STN_Route53')
