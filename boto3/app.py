import boto3
import boto3
region = 'ap-south-1'

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

# s3 = boto3.client('s3')
# BUCKET_NAME='dev-ops-course-practice-bucket'

# sesponse = s3.create_bucket(
#         Bucket=BUCKET_NAME,
#         CreateBucketConfiguration={
#             'LocationConstraint': region  # Specify the region
#         }
#     )

# s3.Bucket(BUCKET_NAME).delete()

# s3.Bucket(BUCKET_NAME).download_file('test.txt', 'text.txt')

# ssm = boto3.client('ssm', region_name=region)

# response = ssm.get_parameter(Name='sample-parameter', WithDecryption=True)

# print(response['Parameter']['Value'])

import pandas

df = pandas.read_csv('https://dev-ops-course-practice-bucket.s3.ap-south-1.amazonaws.com/test.csv')

print(df.head())