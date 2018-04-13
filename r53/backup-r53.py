import boto3

client = boto3.client("route53")

zones_output = client.list_hosted_zones()

print zones_output
