import json
import os
import smtplib
from email.message import EmailMessage
import ssl
from dotenv import load_dotenv 
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI , Request


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv('.env')

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIEVER = os.getenv("EMAIL_RECIEVER")

@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.post("/send")
async def read_item(request : Request):
    dataobj = await request.json()  # converts the request body to dict object
    datadata = dataobj['data']
    anydata = json.loads(datadata['data'])
    # print(anydata)
    msg = EmailMessage()
    msg['Subject'] = f'{anydata["name"]} visited my website'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_RECIEVER

    body = f"name : {anydata['name']} , organisation : {anydata['organisation']}, email : {anydata['email']}, phone : {anydata['phone']}, comment : {anydata['comment']}"

    msg.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_RECIEVER, msg.as_string())
    
    return {"status": 'success'}





