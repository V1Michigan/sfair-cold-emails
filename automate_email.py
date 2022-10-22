import smtplib, ssl
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

CONDENSED_TEMPLATE = '''

'''

PERSONAL_SUBJECT = 'Recruit top talent through V1 Startup Fair @ University of Michigan!'
PERSONAL_TEMPLATE = '''
    <html>
        <body>
            <p>Hello {},</p>

                <p>My name is {}, and I’m a sophomore at the University of Michigan. I’m reaching out to invite you to <b>V1 Startup Fair</b> on <b>November 16</b> – we’d love {} to be a part of it!</p>

                <p>Last year, we connected over <b>200</b> students with <b>17</b> high-growth startups from pre-seed to Series C, with over <b>25</b> offers extended. This year, we’re looking to connect even more students with great companies like yours.</p>

                <p>{} will be able to recruit top <b>engineers, designers,</b> and <b>product managers</b> for intern/new grad positions through virtual career booths, and we’ll be <b>setting up 1:1s</b> with the best candidates for you.</p>

                <p>We’re looking to finalize companies attending by <b>October 21</b>. Attached is our prospectus with more info at <a href='https://startupfair.v1michigan.com'>https://startupfair.v1michigan.com</a>. Please reach out if you have any questions. Looking forward to hearing from you soon!</p>

            <p>Best,<br>{}</p>
        </body>
    </html>
    '''

def send_email(email_from, password, from_name, subject, content, email_to):
    email_message = MIMEMultipart()
    email_message['From'] = from_name
    email_message['To'] = email_to
    email_message['Subject'] = subject

    email_message.attach(MIMEText(content, "html"))
    email_string = email_message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)

if __name__ == '__main__':
    subject, content = format_email(FULL_NAME, "Mage", "Tommy")
    send_email(EMAIL, PASSWORD, FULL_NAME, subject, content, "shrey150@yahoo.com")