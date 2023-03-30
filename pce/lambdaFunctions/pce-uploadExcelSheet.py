import boto3  
from botocore.exceptions import NoCredentialsError  
import pandas as pd 
 
# Set the AWS credentials  
ACCESS_KEY = 'your_access_key'  
SECRET_KEY = 'your_secret_key' 
 
# Set the S3 bucket name and file name  
BUCKET_NAME = 'lca-aih-cl-v2-qnabot-1fdkl84xbf4p8-testallbucket-oo9ym7ezc3rr'  
FILE_NAME = 'your_file_name.xlsx' 
 
# Set the allowed file extensions  
ALLOWED_EXTENSIONS = {'xlsx'} 
 
def allowed_file(filename):  
    """  
    Check if the file has an allowed extension  
    """  
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
 
def upload_to_aws(local_file, bucket, s3_file):  
    """  
    Upload a local file to AWS S3  
    """  
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,  
                      aws_secret_access_key=SECRET_KEY) 
 
    try:  
        s3.upload_file(local_file, bucket, s3_file)  
        print("Upload Successful")  
        return True  
    except FileNotFoundError:  
        print("The file was not found")  
        return False  
    except NoCredentialsError:  
        print("Credentials not available")  
        return False 
 
def process_excel_file(file_path):  
    """  
    Process the uploaded Excel file  
    """  
    try:  
        # Load the Excel file using Pandas  
        df = pd.read_excel(file_path) 
 
        # Verify the file contains valid data and has the correct format  
        # You can add your own validation logic here 
 
        # Upload the file to AWS S3  
        upload_to_aws(file_path, BUCKET_NAME, FILE_NAME)  
        return True  
    except Exception as e:  
        print(f"Error processing file: {e}")  
        return False 
 
if __name__ == '__main__':  
    # Get the file path from the user  
    file_path = input("Please enter the file path: ") 
 
    # Check if the file has an allowed extension  
    if not allowed_file(file_path):  
        print("Invalid file extension. Only .xlsx files are allowed.")  
    else:  
        # Process the Excel file  
        if process_excel_file(file_path):  
            print("File uploaded successfully.")  
        else:  
            print("Error processing file.")  