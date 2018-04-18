import boto3
import re

client = boto3.client("route53")

# json would be your reponse to play with
json = client.list_hosted_zones()

# hosted_zones is just well...your hosted zones
hosted_zones = json['HostedZones']

regexp = re.compile("/hostedzone/(.*)$")
#zone_ids = []

for hosted_zone in hosted_zones:
	#zone_ids.append
	print(regexp.search(hosted_zone['Id']).group(1))

#print(zone_ids) # this should have all that you need :)

# 's' is the string you're trying to parse.
# 'first' is the beginning character
# 'last' is the end character

#def find_between(s, first, last):
#    try:
#        start = s.index(first) + len(first)
#        end = s.index(last, start)
#        return s[start:end]
#    except ValueError:
#        return ""

#print find_between(str(zones_output), "e/", "',")
