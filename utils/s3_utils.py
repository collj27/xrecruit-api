import boto3


def create_presigned_url(object_id, bucket, object_prefix):
    # Choose AWS CLI profile, If not mentioned, it would take default
    object_name = object_prefix + object_id + ".jpg"
    expiration = 600
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3', region_name="us-east-1", config=boto3.session.Config(signature_version='s3v4', ))
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except Exception as e:
        print(e)
        return "Error"
    # The response contains the presigned URL
    print(response)
    return response

