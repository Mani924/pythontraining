import boto3
import pandas as pd
from io import StringIO
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def lambda_handler(event, context):
    # Get the S3 bucket and key from the event
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    # Read the CSV file from S3
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
    csv_content = response['Body'].read().decode('utf-8')

    # Convert the CSV content to HTML using Pandas
    df = pd.read_csv(StringIO(csv_content))
    html_content = df.to_html()

    # Send the email with the HTML content using SMTP
    recipient_email = '<recipient-email-address>'
    sender_email = '<sender-email-address>'
    password = '<sender-email-password>'
    subject = 'HTML email from Lambda'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    part = MIMEText(html_content, 'html')
    msg.attach(part)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
    except Exception as e:
        print(e)
    else:
        print("Email sent!")
