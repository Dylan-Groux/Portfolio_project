from dotenv import load_dotenv
import os


load_dotenv()

#Variable pour l'accès SMTP de gmail 
email_sender = os.getenv("MAIL_USERNAME")
email_password = os.getenv("MAIL_PASSWORD")

print({email_sender})
print({email_password})
