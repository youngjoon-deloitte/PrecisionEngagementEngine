#Take campaignID, campaignName, campaignDescription, startTime, endTime, timeZone, quietTimeStart, quietTimeEnd, journeyRecordID from the event
#Take projectID from environment variable
# Store the variables in a pce-campaignDetails dynamoDB table with campaignID as the partition key.
#Get lambdaFunctionURI from DynamoDB table pce-journeyDetails using journeyRecordID as the partition key.
#Invoke the lambda function using the lambdaFunctionURI and the projectId, startTime, endTime, timeZone, quietTimeStart, quietTimeEnd as the payload. Capture the journeyID response
#Store journeyID response to the pce-campaignDetails dynamoDB table with campaignID as the partition key.

import json
import boto3
import datetime
import time
import calendar
import random
import string
import os
import logging
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))
    logger.info("Received context: " + str(context))
    try:
        journeyRecordID = event['journeyRecordID']
        campaignID = event['campaignID']
        campaignName = event['campaignName']
        campaignDescription = event['campaignDescription']
        startTime = event['startTime']
        endTime = event['endTime']
        timeZone = event['timeZone']
        quietTimeStart = event['quietTimeStart']
        quietTimeEnd = event['quietTimeEnd']
        projectId = os.environ['projectId']
        lambdaFunctionURI = ''
        journeyID = ''
        response = ''
        #Get lambdaFunctionURI from DynamoDB table pce-journeyDetails using journeyRecordID as the partition key.
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('pce-journeyDetails')
        response = table.get_item(
            Key={
                'journeyRecordID': journeyRecordID
            }
        )        
        lambdaFunctionURI = response['Item']['lambdaFunctionURI']
        #Invoke the lambda function using the lambdaFunctionURI and the projectId, startTime, endTime, timeZone, quietTimeStart, quietTimeEnd as the payload. Capture the journeyID response
        payload = {
            'projectId': projectId,
            'startTime': startTime,
            'endTime': endTime,
            'timeZone': timeZone,
            'quietTimeStart': quietTimeStart,
            'quietTimeEnd': quietTimeEnd
        }
        client = boto3.client('lambda') 
        response = client.invoke(
            FunctionName=lambdaFunctionURI,
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps(payload)
        )
        logger.info("Response: " + str(response))
        journeyID = response['Payload'].read().decode('utf-8')
        journeyID = json.loads(journeyID)
        journeyID = journeyID['journeyID']
        #Store journeyID response to the pce-campaignDetails dynamoDB table with campaignID as the partition key.
        table = dynamodb.Table('pce-campaignDetails')
        response = table.put_item(
            Item={
                'campaignID': campaignID,
                'campaignName': campaignName,
                'campaignDescription': campaignDescription,
                'startTime': startTime,
                'endTime': endTime,
                'timeZone': timeZone,
                'quietTimeStart': quietTimeStart,
                'quietTimeEnd': quietTimeEnd,
                'journeyRecordID': journeyRecordID,
                'journeyID': journeyID
            }
        )
        logger.info("Response: " + str(response))
        return journeyID
    except Exception as e:
        logger.error("Exception: " + str(e))
        raise e 