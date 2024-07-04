import boto3
from botocore.exceptions import ClientError

s3 = boto3.client(
    's3',
    aws_access_key_id='put your aws access key',
    aws_secret_access_key='put your aws secret key'
)
bucket_name = 'imagemanagment'

def upload_to_s3(file, image_id):
    s3.upload_fileobj(file.file, bucket_name, f"images/{image_id}_{file.filename}")

def delete_from_s3(image_id, filename):
    try:
        s3.delete_object(Bucket=bucket_name, Key=f"images/{image_id}_{filename}")
    except ClientError as e:
        raise Exception(f"Failed to delete from S3: {str(e)}")
