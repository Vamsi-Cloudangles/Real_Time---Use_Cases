import os
import pandas as pd 
import boto3
import csv

client = boto3.client(
    's3',
    aws_access_key_id='AKIA3YG72WSKDULO5WJ4',
    aws_secret_access_key='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',
    region_name='us-east-1'
)

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name=file_name
    response=client.upload_file(file_name, bucket, 'cleaned_data/'+ object_name, ExtraArgs=args)
    print(response)



def dvc():
    upload_files('cleaned.csv', 'sagemaker-vamsi')
    os.system('pip3 install dvc[s3]')

    os.system("git init")
    os.system("dvc init -f")
    os.system('dvc config core.analytics false')
    os.system("dvc remote add -d storage s3://sagemaker-vamsi/dvc/")
    os.system("dvc add cleaned.csv")
    os.system("git add cleaned.csv.dvc .gitignore")
    print("dvc file is pushing to s3......")
    os.system("dvc push")
    print("done")

