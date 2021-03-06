# This is designed to run as a scheduled Lambda function, and exports your
# Route 53 zone metadata to be backed up


import boto3
import re
import time
import json

def lambda_handler(event, context):
    r53_client = boto3.client('route53')
    s3_client = boto3.client('s3')
    timestamp = time.strftime("%Y-%m-%d @ %H:%M:%S")

    hz_json = r53_client.list_hosted_zones()
    hosted_zones = hz_json['HostedZones']

    regexp = re.compile("/hostedzone/(.*)$")

    r53_backup = []

    for hosted_zone in hosted_zones:
        zone_id = regexp.search(hosted_zone['Id']).group(1)
        r53_backup.append(r53_client.list_resource_record_sets(HostedZoneId=zone_id))
        s3_client.put_object(
            Body=(json.dumps(r53_backup, indent=4, sort_keys=False)),
            Bucket='[BUCKET NAME]',
            Key='r53backup ' + timestamp
        )
    #print(json.dumps(r53_backup, indent=4, sort_keys=False))
