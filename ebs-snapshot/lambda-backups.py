# Backup all in-use volumes in all regions

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all in-use volumes in all regions  
    result = ec2.describe_volumes( VolumeIds=[
        #'vol-06edc3097410fe5d4', # Triton C (TESTING)
        'vol-00bcbc49', # Adonis D
        'vol-b7f5e8fb', # Athena D
        'vol-0cedab4cc90daa39a', # Atlas M
        'vol-0d88c2c678968856d', # Atlas L
        'vol-0f2857c60be51ad35', # Gaia C
        'vol-8c0b7bcf', # Gaia D
        'vol-062db5b7f9c9a2d6b', # Hebe C 
        'vol-67661510', # Hebe D
        'vol-fb31482a', # Hermes B
        'vol-d618c845', # Hermes C
        'vol-06549db5aa5d4277f', # Hermes D
        'vol-0db623ad46a082e9d', # Zelus C
        'vol-0fd6a90020a728dd6', # Zelus D
        'vol-0695697264e282de6', # Zeus B
        ]
    )
    
    for volume in result['Volumes']:
        print "Backing up %s in %s" % (volume['VolumeId'], volume['AvailabilityZone'])
        
        # Create snapshot
        result = ec2.create_snapshot(VolumeId=volume['VolumeId'],Description='Created by Lambda backup function ebs-backup')
        
        # Get snapshot resource 
        ec2resource = boto3.resource('ec2', region_name='us-east-1')
        snapshot = ec2resource.Snapshot(result['SnapshotId'])
        
        volumename = 'N/A'
        
        # Find name tag for volume if it exists
        if 'Tags' in volume:
            for tags in volume['Tags']:
                if tags["Key"] == 'Name':
                    volumename = tags["Value"]
        
        # Add volume name to snapshot for easier identification
        snapshot.create_tags(Tags=[{'Key': 'Name','Value': volumename}])

