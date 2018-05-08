import boto3

s3 = boto3.client('s3')

# reads all files older than 30 days and pulls key (filename), appending to a list
files = []

files.append()

# deletes files specified in list from last command
for file in files:
    s3.delete_objects(
        Bucket = 'alex-stn-testing'
        Delete ={
            'Objects': [
                {
                    'Key': '{}'.format(file)
                },
            ],
        },
    )
