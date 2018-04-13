import boto3

client = boto3.client("route53")

zones_output = client.list_hosted_zones()

# 's' is the string you're trying to parse. 
# 'first' is the beginning character
# 'last' is the end character

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

print find_between(str(zones_output), "e/", "',")


