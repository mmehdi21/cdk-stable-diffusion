import boto3
import uuid
import os

s3  = boto3.client('s3')
transcribe = boto3.client('transcribe')

OUTPUT_BUCKET_NAME = os.environ['OutputBucketName']

def lambda_handler(event, context):
    try:
        file_bucket = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        file_name = file_key.split('.')[0]
        object_url = 'https://s3.amazonaws.com/{0}/{1}'.format(file_bucket, file_key)
        response = transcribe.start_transcription_job(
        TranscriptionJobName="Job-{}-{}".format(file_name, str(uuid.uuid4()).split('-')[0]),
        IdentifyLanguage= True,
        Media={
            'MediaFileUri': object_url
        },
        OutputBucketName=OUTPUT_BUCKET_NAME,
        OutputKey="{}.json".format(file_name)
        )
        return ""
    except Exception as e:
        raise e
