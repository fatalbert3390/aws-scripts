import boto3
import re
import time

r53_client = boto3.client('route53')
s3_client = boto3.client('s3')
timestamp = time.strftime("%Y-%m-%d @ %H:%M:%S")

# json would be your reponse to play with
hz_json = r53_client.list_hosted_zones()

# hosted_zones is just well...your hosted zones
hosted_zones = hz_json['HostedZones']

regexp = re.compile("/hostedzone/(.*)$")

for hosted_zone in hosted_zones:
    zone_id = regexp.search(hosted_zone['Id']).group(1)
    backup_json = r53_client.list_resource_record_sets(HostedZoneId=zone_id)
    #s3_client.put_object(
    #    Body=b'%s' % (backup_json),
    #    Bucket='alex-stn-testing',
    #    Key='r53backup ' + timestamp
    #)
