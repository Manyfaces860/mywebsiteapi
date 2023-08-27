import os
import smtplib
from email.message import EmailMessage
from typing import Union
import ssl
# from dotenv import load_dotenv , find_dotenv

from fastapi import FastAPI

app = FastAPI()
# dotenv_path = find_dotenv()
# load_dotenv(dotenv_path)

EMAIL_ADDRESS = 'abhishek13shadow@gmail.com'
EMAIL_PASSWORD = 'rsqoztvahmcbxbdu'
EMAIL_RECIEVER = 'agblion9@gmail.com'

# EMAIL_ADDRESS = os.getenv('EMAIL_USER')
# EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
# EMAIL_RECIEVER = os.getenv("EMAIL_RECIEVER")

@app.get("/")
def read_root():
    return {"Hello": EMAIL_ADDRESS}


@app.get("/send")
def read_item():

    msg = EmailMessage()
    msg['Subject'] = 'trial email no.3'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_RECIEVER

    msg.set_content('This is a first email')
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_RECIEVER, msg.as_string())
    
    return {"status": 'success'}





