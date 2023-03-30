import boto3  
from botocore.exceptions import NoCredentialsError  
import pandas as pd  
import hashlib

# Set the AWS credentials  
ACCESS_KEY = 'your_access_key'  
SECRET_KEY = 'your_secret_key'

# Set the S3 bucket name and file name  
BUCKET_NAME = 'your_bucket_name'  
FILE_NAME = 'your_file_name.xlsx'

# Set the allowed file extensions  
ALLOWED_EXTENSIONS = {'xlsx'}

# Set the database or file where the mapping will be stored  
# For simplicity, we will use a Python dictionary to store the mapping in memory  
mapping = {}

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

def tokenize_data(data):  
    """  
    Tokenize personal information contained in the data  
    """  
    # Convert the data to a string  
    data_str = str(data)

    # Tokenize the string using SHA-256 hashing algorithm  
    hashed_data = hashlib.sha256(data_str.encode()).hexdigest()

    return hashed_data

def process_excel_file(file_path):  
    """  
    Process the uploaded Excel file  
    """  
    try:  
        # Load the Excel file using Pandas  
        df = pd.read_excel(file_path)

        # Tokenize all personal information contained in the data  
        for column in df.columns:  
            if column.lower() in ['name', 'address', 'phone', 'email']:  
                df[column] = df[column].apply(tokenize_data)

                # Store the mapping of tokenized data to original data  
                for i, val in df[column].items():  
                    mapping[val] = df.at[i, column]

        # Upload the tokenized data to AWS S3  
        upload_to_aws(file_path, BUCKET_NAME, FILE_NAME)  
        return True  
    except Exception as e:  
        print(f"Error processing file: {e}")  
        return False

def retrieve_original_data(tokenized_data):  
    """  
    Retrieve the original data from the tokenized data  
    """  
    return mapping.get(tokenized_data)

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

            # Test the retrieve_original_data function  
            tokenized_data = list(mapping.keys())[0]  
            original_data = retrieve_original_data(tokenized_data)  
            print(f"Original data: {original_data}")  
        else:  
            print("Error processing file.")  