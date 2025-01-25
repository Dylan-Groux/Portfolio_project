from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
import os

# Création de l'app Flask
app = Flask(__name__, static_folder='portfolio/static')
CORS(app)

# Configuration du serveur mail 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

if __name__ == '__main__':
    app.run()  # Retirer debug=True