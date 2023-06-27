import json
import boto3
import uuid


transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    print("i m lw...")
    
    filename = event['Records'][0]['s3']['object']['key']
    bucketname = event['Records'][0]['s3']['bucket']['name']
    
    url = "s3://" + bucketname + "/" + filename
    
    myuuid = uuid.uuid1().int
    
    response = transcribe.start_transcription_job(
                 
                    TranscriptionJobName="mylwaudiojob" + "-" + str(myuuid), 
                    LanguageCode='en-US',
                    MediaFormat='mp3',
                    Media={
                        'MediaFileUri': url,
                            },
                    OutputBucketName="lws3transcribetest123",
                    OutputKey="mylwaudiojob" + "-" + str(myuuid) + ".json"
                    )
    
    print(response)
    
    
    
    
    
