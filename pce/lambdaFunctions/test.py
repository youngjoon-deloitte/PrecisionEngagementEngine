import boto3

#lambda function to take campaignID from the event and return the campaign status from the dynamoDB table pce-campaignDetails. 
def lambda_handler(event, context):
    
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pce-campaignDetails')
    campaignID = event['campaignID']
    response = table.get_item(
        Key={
            'campaignID': campaignID
        }
    )
    item = response['Item']
    #return error prompt if campaignID is not found
    if 'campaignID' not in response:
        return {
            'statusCode': 400,
            'body': "Campaign ID not found"
        }
    return item