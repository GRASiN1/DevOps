import boto3


s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

# s3 = boto3.client('s3')
BUCKET_NAME='dev-ops-course-practice-bucket'
region = 'ap-south-1'

# sesponse = s3.create_bucket(
#         Bucket=BUCKET_NAME,
#         CreateBucketConfiguration={
#             'LocationConstraint': region  # Specify the region
#         }
#     )

# s3.Bucket(BUCKET_NAME).delete()

s3.Bucket(BUCKET_NAME).download_file('test.txt', 'text.txt')