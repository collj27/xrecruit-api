import boto3


def create_presigned_url(player_id):
    # Choose AWS CLI profile, If not mentioned, it would take default
    # boto3.setup_default_session(profile_name='personal')
    bucket = "xrecruit-player-images"
    object_name = "player_" + player_id + ".jpg"
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

