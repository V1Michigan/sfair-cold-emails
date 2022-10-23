import smtplib, ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

FULL_NAME = os.getenv('FULL_NAME')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

if FULL_NAME is None or EMAIL is None or PASSWORD is None:
    raise Exception('Environment variables not set')

def format_email(name, company, recruiter_name, email_type="personal"):
    if email_type == "personal":
        return (
            PERSONAL_SUBJECT,
            PERSONAL_TEMPLATE.format(
                recruiter_name,
                name,
                company,
                company,
                name.split()[0],
            )
        )

PERSONAL_SUBJECT = 'Recruit top talent through V1 Startup Fair @ University of Michigan!'
with open('templates/personal.html', 'r') as f:
    PERSONAL_TEMPLATE = f.read()

def send_email(email_from, password, from_name, subject, content, email_to):
    email_message = MIMEMultipart()
    email_message['From'] = from_name
    email_message['To'] = email_to
    email_message['Subject'] = subject

    email_message.attach(MIMEText(content, "html"))
    pdf = MIMEApplication(open('assets/prospectus.pdf', 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment', filename='V1 Startup Fair Prospectus.pdf')
    email_message.attach(pdf)
    email_string = email_message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)

if __name__ == '__main__':
    confirm = input('Are you sure you want to send emails? (y/n)\t')
    if confirm != 'y': exit()
    subject, content = format_email(FULL_NAME, "Mage", "Tommy")
    send_email(EMAIL, PASSWORD, FULL_NAME, subject, content, "shrey150@yahoo.com")