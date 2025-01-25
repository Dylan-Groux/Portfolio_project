from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration du serveur mail 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_DEBUG'] = True

app.config['MAIL_USERNAME'] = 'smtpredar@gmail.com'
app.config['MAIL_PASSWORD'] = 'cvgl yoab izyi rvws'
app.config['MAIL_DEFAULT_SENDER'] = 'smtpredar@gmail.com'

mail = Mail(app)

def create_app():
    #Initialisation de l'app FLASK
    app.config.from_object('config')
    return app