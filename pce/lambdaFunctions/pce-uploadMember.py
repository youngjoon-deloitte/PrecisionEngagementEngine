#read csv file from s3 upload trigger. Each line of csv file is pinpoint endpoint
#capture csv file name and store the value before "-" in a variable event-type
#create a new event to record for endpoint from csv file and pass event-type and endpoint to put_event pinpoint api
#return response to the client

import json
import boto3
import csv
import logging
import os
from botocore.exceptions import ClientError
#from protegrityUtils import protegrity

# Create protegrity Object
#PROTEGRITY_HOST = os.environ['PROTEGRITY_HOST']
#PROTEGRITY_PWD = os.environ['PROTEGRITY_PWD']
#PROTEGRITY_UM = os.environ['PROTEGRITY_UM']
#protegrity_obj = protegrity.Protegrity(PROTEGRITY_HOST, PROTEGRITY_UM, PROTEGRITY_PWD)

# Setting Logger Level to INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['Lier_MemberData_TBL_NM'])

# resources for starting the journey
s3_resource = boto3.resource('s3')
client = boto3.client('logs')
pinpoint_client = boto3.client('pinpoint')
ApplicationId = os.environ['ApplicationId']
Universal_Timezone = os.environ['Timezone']

def load_csv_Data_from_s3_and_match(Bucket, Key):
    s3_object = s3_resource.Object(Bucket, Key)
    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()
    lines = csv.reader(data, delimiter='|')
    headers = next(lines)
    print('headers: %s' % (headers))
    for line in lines:
        MemberNumber, PhoneNumber, F02, F03 = line[3], line[6], line[28], line[29]
        #Website_Link, Virtual_Card, PCPName_First, PCPName_Last, PCP_Phone, Member_Services_Num, Member_Services_Days, Member_Services_Hours, Provider_Finder, Health_Plan, Url4, Doctor_Url = line[17], line[28],line[29],line[4], line[2], line[3], line[1], line[17], line[28],line[29]
        print(line)
        response = phonenumbervalidate('US', PhoneNumber)
        responsecode = response['NumberValidateResponse']['PhoneTypeCode']
        responsetype = response['NumberValidateResponse']['PhoneType']
        if responsecode == 0 or responsecode == 2 or responsecode == 5:
            res = put_events_function(MemberNumber, PhoneNumber, Universal_Timezone, F02, F03, EventType="User.Lier")
            print(res)
        else:
            logger.info(f'Phone Number validation Type: {responsetype}' )
            logger.info(f'Phone Number validation Code: {responsecode}' )
            logger.info(f'No Endpoint created for phone number:{PhoneNumber}')
            # update validation filed in dynamoDB
            update_response = table.update_item(Key={'PhoneNumber': '+1'+ PhoneNumber},
                                                UpdateExpression='SET Error_Message = :val1, Error_Type = :val2, Error_Code = :val3' ,
                                                ExpressionAttributeValues={":val1": "Phone Number Validation Failed",
                                                                          ":val2": responsetype,
                                                                          ":val3": responsecode})


def phonenumbervalidate(code,number):
    num = number 
    response = pinpoint_client.phone_number_validate(
    NumberValidateRequest={
        'IsoCountryCode': code,
        'PhoneNumber': '+1' + num
    }
    )
    return response


def put_events_function(MemberNumber, PhoneNumber, Timezone, F02, F03, EventType):
    MemberNumber = str(MemberNumber)
    print(MemberNumber)
    PhoneNumber = str(PhoneNumber)
    print(PhoneNumber)
    response = pinpoint_client.put_events(
        ApplicationId=ApplicationId,
        EventsRequest={
            'BatchItem': {
                MemberNumber: {
                    'Endpoint': {
                        "outreachChannel": "SMS",
                        'Demographic': 
                                { 'Timezone': Timezone },
                        "Address": "+1" + PhoneNumber,
                        'EffectiveDate': '2022-11-23T04:33:27+09:00',
                        'EndpointStatus': 'ACTIVE',
                        'OptOut': 'NONE',
                        'User': {
                            'UserId': MemberNumber,
                            'UserAttributes': {
                                'F02': [
                                    F02
                                ],
                                'F03': [
                                    F03
                                ]
                            }
                        }},
                    'Events': {
                        'Stage': {
                            'EventType': EventType,
                            'Timestamp': '2022-11-23T04:33:27+09:00'
                        }
                    }
                }
            }})
    return response
    #FirstName
    #Website_Link or get care
    #Virtual_Card
    #PCPName_First
    #PCPName_Last
    #PCP_Phone
    #Member_Services_Num
    #Member_Services_Days
    #Member_Services_Hours
    #Provider_Finder_URL
    #Health_Plan
    #Url4
    #Doctor_Url
    #Nurseline_Number
    #PCP_1st_Ref
    #PCP_2nd_Ref
    #Get_Care_URL
    #Health_Plan_2nd_Ref

def lambda_handler(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']  # fetch bucket name
    csv_file_name = event['Records'][0]['s3']['object']['key']  # fetch file name
    csv_object = s3_client.get_object(Bucket=bucket, Key=csv_file_name)  # invoking the method
    print(bucket)
    print(csv_file_name)
    # print(type(csv_object))
    file_reader = csv_object['Body'].read().decode("utf-8")  # decode the deictionary csv_object 
    print(type(file_reader))
    print(file_reader)
    users = file_reader.split("\n")  # to make each element split to read it 
    # print(users)
    users = list(filter(None, users))  # to remove empty element from the list
    print(users)

    for user in users[1:]:
        user_data = user.split("|")
       
        #table.put_item(Item=protegrity_obj.encrypt_json({
        table.put_item(Item={
            "Record_Id": user_data[0],
            "Batch_Id": user_data[1],
            "Customer_Name": user_data[2],
            "Member_Id": user_data[3],
            "FirstName": user_data[4],
            "LastName": user_data[5],
            "PhoneNumber": '+1' + user_data[6],
            "Phone_2": user_data[7],
            "Phone_3": user_data[8],
            "Phone_4": user_data[9],
            "Phone_5": user_data[10],
            "Gender": user_data[11],
            "DOB": user_data[12],
            "Address1": user_data[13],
            "Address2": user_data[14],
            "City": user_data[15],
            "State": user_data[16],
            "ZipCode": user_data[17],
            "Language": user_data[18],
            "Application_Name": user_data[19],
            "AG_Group": user_data[20],
            "AG_Product": user_data[21],
            "AG_Market": user_data[22],
            "AG_CSPI_ID": user_data[23],
            "Portal_LOB": user_data[24],
            "Recert_DT": user_data[25],
            "Renewal_Month": user_data[26],
            "County": user_data[27],
            "F02":user_data[28],
            "F03":user_data[29],
            "F04":user_data[30],
            "F05":user_data[31],
            "F06":user_data[32],
            "F07":user_data[33],
            "F08":user_data[34],
            "F09":user_data[35],
            "Email": user_data[36],
            "F11":user_data[37],
            "F12":user_data[38],
            "F13":user_data[39],
            "F14":user_data[40],
            "F15":user_data[41],
            "F16":user_data[42],
            "F17":user_data[43],
            "F18":user_data[44],
            "F19":user_data[45],
            "F20":user_data[46],
            "unqMemberId":user_data[47],
            "Preffered_Language":user_data[48],
            "Timezone": Universal_Timezone,
            "Total_Messages_Received": 0,
            "Total_Messages_Sent": 0,
            "Average_Response_Time": 0,
            "STOP_Request": 'No',
            "WRONG_Request": 'No',
            "PCP_Request": 'No',
            "NO_PCP_Request": 'No',
            "YES_Request": 'No',
            "NO_Request": 'No',
            "HELP_Request": 'No',
            "CALL_Request": 'No',
            "SENSITIVE_Request": 'No',
            "UNExpected_Request": 'No'

        })
        #}))

    print("Table udpated")
    load_csv_Data_from_s3_and_match(Bucket=bucket, Key=csv_file_name)
    return "success"

