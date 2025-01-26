# config.py
import os

class Config:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_DEBUG = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    
#app.config['MAIL_USERNAME'] = 'smtpredar@gmail.com'
#app.config['MAIL_PASSWORD'] = 'cvgl yoab izyi rvws'
#app.config['MAIL_DEFAULT_SENDER'] = 'smtpredar@gmail.com'
