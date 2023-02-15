import json
import logging
import boto3
import os
import threading 
from boto3.dynamodb.conditions import Key
from datetime import datetime,time,timedelta
from botocore.exceptions import ClientError
import calendar
from operator import itemgetter



#Setting Logger Level to  INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Get Pinpoint and Personalize boto3 API's
pinpoint_client = boto3.client('pinpoint')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['Lier_MemberData_TBL_NM'])
template_table = dynamodb.Table(os.environ['LIER_SMSTemplate_TBL_NM'])
mapping_table = dynamodb.Table(os.environ['LIER_SMSMapping_TBL_NM']) 
OUTBOUND_PHN_NM = os.environ['OUTBOUND_PHN_NM']

#from protegrityUtils import protegrity
from errorUtils import exponentialBackoff

# Create protegrity Object
#PROTEGRITY_HOST = os.environ['PROTEGRITY_HOST']
#PROTEGRITY_PWD = os.environ['PROTEGRITY_PWD']
#PROTEGRITY_UM = os.environ['PROTEGRITY_UM']
#protegrity_obj = protegrity.Protegrity(PROTEGRITY_HOST, PROTEGRITY_UM, PROTEGRITY_PWD)


# Send Message Definition
@exponentialBackoff.retry_with_backoff(retries=6)
def send_sms_message(
        pinpoint_client, 
        project_id,
        endpoint_id, 
        message_type,
        Message,
        destination_number):
    try:
        response = pinpoint_client.send_messages(
            ApplicationId=project_id,
            MessageRequest={
                'Endpoints': {endpoint_id :{}},
                'MessageConfiguration': {
                    'SMSMessage': {
                        'MessageType': message_type,
                        'Body': Message,
                        'OriginationNumber': destination_number}
                                        }
            })
        print(response)
    except ClientError:
        logger.exception("Couldn't send message.")
        raise
    else:
        print(f"MessageResponse:{response}")
        return response['MessageResponse']['EndpointResult'][endpoint_id]['MessageId'], response['MessageResponse']['EndpointResult'][endpoint_id]['StatusCode']
        
def lambda_handler(event, context):
    print("event",event)
    for key in list(event['Endpoints'].keys()):
        print(key)
        # print(event['Endpoints'][key]['Address'])
        UserId = event["Endpoints"][key]["User"]["UserId"]
        # get originat number
        origination_number = event["Endpoints"][key]["Address"]
        user_data = get_user_detail(origination_number)
        Message =  content_driver(user_data, event['Data'] )
        message_id, statusCode = send_sms_message(pinpoint_client,event['ApplicationId'],UserId,'TRANSACTIONAL',Message ,OUTBOUND_PHN_NM)
        print(message_id, statusCode)
        # process message and update in dynamoDB
        process_and_update_message_log({"messageId": message_id, "messageTime": datetime.utcnow(),
                                        "message": event['Data'], "messageType": "Sent" }, origination_number)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
def content_driver(user_data, Data):
    print(user_data)
    print(user_data['F02'])
    print(user_data['F03'])
    if Data == 'Welcome_Message':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'Welcome_Msg_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)
    if Data == 'C1_M1':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C1_M1_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)
    if Data == 'C1_M2':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C1_M2_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)     
    if Data == 'C1_M3':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C1_M3_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)         
    if Data == 'C2_M1':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C2_M1_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details) 
    if Data == 'C2_M2':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C2_M2_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)         
    if Data == 'C2_M3':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C2_M3_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)         
    if Data == 'C3_M1':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C3_M1_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)  
    if Data == 'C3_M2':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C3_M2_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details) 
    if Data == 'C3_M3':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C3_M3_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)   
    if Data == 'C4A_M1':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C4A_M1_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)    
    if Data == 'C4A_M2':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C4A_M2_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details) 
    if Data == 'C4A_M3':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C4A_M3_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)  
    if Data == 'C4B_M1':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C4B_M1_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)  
    if Data == 'C4B_M2':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C4B_M2_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)
    if Data == 'C4B_M3':
        if user_data['Language'].lower() == 'eng':
            template_details = get_template_detail(templateName = 'C4B_M3_En')
            Message = template_details['Content']
            print(user_data['State'])
            mapping_details = get_mapping_detail(applicationName = user_data['applicationName'],partialLOB = user_data['partialLOB'] )
            Message = content_format(Message,user_data,mapping_details)         
    return Message   
    
def content_format(Message,user_data,mapping_details):
    Message = Message.format(
        HealthPlan = mapping_details['Health_Plan_Name_1st_Ref'], 
        MemberServicesNum =mapping_details['Member_Services_Number'],
        MemberServicesHours = mapping_details['MS_Hours_Of_Operation'],
        NurseLineNum = mapping_details['Nurseline_Number'],
        MbrNameFirst = user_data['FirstName'], 
        ProviderFinderUrl = mapping_details['Provider_Finder_URL'],
        ProviderFinderName = user_data['F14'], 
        PCP_1st_ref = mapping_details['PCP_1st_Ref'],
        GetCareUrl = mapping_details['Get_Care_URL'],
        PCP_2nd_ref = mapping_details['PCP_2nd_Ref'],
        HealthPlanAbbr = mapping_details['Health_Plan_2nd_Ref'],
        PcpNameFirst = user_data['F14'], 
        PcpNameLast = user_data['F15'], 
        PcpPhone = user_data['F16'],
        HealthPlanWebsite = mapping_details['Plan_Website'],
        Case_Manager = mapping_details['Case_Manager'],
        VirtualCardURL = mapping_details['Virtual_Card_URL'],
        LanguageSwitch = "N/A")
    return Message 
    
def process_and_update_message_log(message_event, phone_number):
    print("process_event : {} and phone_number : {}".format(message_event, phone_number))
    # function to get user detail to update data
    member_detail = get_user_detail(phone_number)
    # function to get mesg log update status
    msg_log_status = update_msg_log(phone_number, member_detail, message_event)
    print("message log updated in dynamoDB")
    return  "SUCCESS"
    
def get_user_detail(phone_number):
    # get item based on primary key of member id
    response = table.query(
    IndexName='PhoneNumber-index',
    KeyConditionExpression=Key('PhoneNumber').eq(phone_number))
    newlist = sorted(response['Items'], key=itemgetter('F03'),reverse = True)
    newlist = newlist[0]
    
    #member_detail = table.get_item(Key={"PhoneNumber": phone_number}).get("Item")
    #return protegrity_obj.decrypt_json(member_detail)
    print("Userdata printing")
    print(newlist)
    return newlist
    
def get_template_detail(templateName):
    # get item based on primary key of member id
    return template_table.get_item(Key={"templateName": templateName}).get("Item")
    
def get_mapping_detail(applicationName,partialLOB):
    # get item based on primary key of member id
    return mapping_table.get_item(Key={"applicationName": applicationName,"partialLOB":partialLOB}).get("Item")    
    
def update_msg_log(phone_number, member_detail, message_event):
    # process message from event and database and collect avg response time
    msg_type = str(message_event.get("messageType")).lower()
    msg_data = message_event.get("message")
    message_id = message_event.get("messageId")
    msg_time = calendar.timegm(message_event.get("messageTime").utctimetuple())
    # get rcv msg count
    total_msg_send = int(member_detail.get("Total_Messages_Sent", 0)) + 1
    # get message detail from dynamoDB
    msg_db_data = member_detail.get("messageLog", [])
    if msg_db_data:
        msg_db_data = sorted(msg_db_data, key=itemgetter('timestamp'))
    # add current msg into old DB message log
    msg_db_data.append({"timestamp": int(msg_time), "message": msg_data, "type": msg_type.title(), "id": message_id})
    # calculate avg response time from message log
    avg_rsp_tm = get_avg_response_time(msg_db_data)
    # update in dynamoDB message log and avg response time
    table.update_item(Key={"unqMemberId": member_detail['unqMemberId']},
                                UpdateExpression="set messageLog = :m, Average_Response_Time = :n, Total_Messages_Sent = :o",
                                ExpressionAttributeValues={":m": msg_db_data, ":n": avg_rsp_tm, ":o": total_msg_send},
                                ReturnValues="UPDATED_NEW")
    return "SUCCESS"
def get_avg_response_time(msg_db_data):
    # collect all resp time in list and then take average
    resp_time = list()
    sent_time = None
    for msg_data in msg_db_data:
        if msg_data.get("type").__eq__("Sent") and not sent_time:
            sent_time = int(msg_data.get("timestamp"))
        if msg_data.get("type").__eq__("Received") and sent_time:
            resp_time.append(int(msg_data.get("timestamp")) - sent_time)
    if resp_time:
        print(resp_time)
        # get avg and return into second
        return int((sum(resp_time) / float(len(resp_time))))
    else:
        return 0