import json
import os
import smtplib
from email.message import EmailMessage
from typing import Union
import ssl
from pydantic import BaseModel
# from dotenv import load_dotenv , find_dotenv
from fastapi.middleware.cors import CORSMiddleware

class Data(BaseModel):
    name: str
    organisation: str
    email: str
    phone: int = None
    comment: str = None

from fastapi import FastAPI , Request

app = FastAPI()
# dotenv_path = find_dotenv()
# load_dotenv(dotenv_path)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EMAIL_ADDRESS = 'abhishek13shadow@gmail.com'
EMAIL_PASSWORD = 'rsqoztvahmcbxbdu'
EMAIL_RECIEVER = 'agblion9@gmail.com'

# EMAIL_ADDRESS = os.getenv('EMAIL_USER')
# EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
# EMAIL_RECIEVER = os.getenv("EMAIL_RECIEVER")

@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.post("/send")
async def read_item(request : Request):
    anydata = await request.json()  # converts the request body to dict object
    # print(anydata)
    msg = EmailMessage()
    msg['Subject'] = 'trial email no.5'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_RECIEVER

    body = f"name : {anydata['name']} , organisation : {anydata['organisation']}, email : {anydata['email']}, phone : {anydata['phone']}, comment : {anydata['comment']}"

    msg.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_RECIEVER, msg.as_string())
    
    return {"status": 'success'}





