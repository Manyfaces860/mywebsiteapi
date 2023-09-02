# mywebsiteapi

this Api can send emails to From EMAIL_SENDER to EMAIL_RECIEVER

To run this api you have to add a .env file to the project folder with EMAIL_SENDER EMAIL_PASSWORD and EMAIL_RECIEVER info inside this .env file.
then run this command -> uvicorn main:app 
then make a post request with data in json format to the '/send' endpoint
