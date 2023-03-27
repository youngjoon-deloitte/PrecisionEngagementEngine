#create a function to take an event from api gateway that has USER_ID, ITEM_ID, EVENT_TYPE, CAMPAIGN_NAME, LANGUAGE, CHANNEL, PURPOSE and send as an object to S3 bucket

#import boto3
#import json
#import os
#import uuid
#import time

#def lambda_handler(event, context):
    #print(event)
    #return {
        

import json

def lambda_handler(event, context):
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }



