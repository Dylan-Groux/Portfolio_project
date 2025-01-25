from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
import os

# Création de l'app Flask
app = Flask(__name__)
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
    app.run(debug=True)

# Fonction pour initialiser l'app
def create_app():
    app.config.from_object('config')
    return app