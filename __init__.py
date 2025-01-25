from flask import Flask, render_template
from flask_mail import Mail
from flask_cors import CORS
import os

# Création de l'app Flask
app = Flask(__name__)
CORS(app)

# Récupère le port à partir des variables d'environnement (si disponible)
port = int(os.environ.get("PORT", 5000))  # Utilise le port dynamique, 5000 en fallback

app.run(host='0.0.0.0', port=port)

# Configuration du serveur mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

# Route de la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
