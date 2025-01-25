# main.py

from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os

# Création de l'app Flask
app = Flask(__name__)
CORS(app)  # Permettre CORS si nécessaire pour des appels API depuis d'autres domaines

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
    return render_template('index.html')  # La page d'accueil avec le formulaire

@app.route('/contact', methods=['POST'])
def contact():
    # Récupérer les données du formulaire
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    sujet = request.form.get('sujet')
    message_content = request.form.get('message')

    # Log des données pour vérification
    app.logger.debug(f'Requête reçue: {name}, {email}, {phone}, {sujet}, {message_content}')

    # Vérification des champs requis
    if not name or not email or not phone or not sujet or not message_content:
        return jsonify({'error': 'Tous les champs sont requis.'}), 400

    # Création du message email
    subject = f"Nouveau message de contact de {name}"
    body = f"Nom: {name}\nEmail: {email}\nTéléphone: {phone}\n\nMessage:\n{message_content}\n Sujet : {sujet}"

    try:
        msg = Message(subject, sender=email, recipients=['smtpredar@gmail.com'])
        msg.body = body
        mail.send(msg)
        return jsonify({"success": "Message envoyé avec succès."}), 200
    except Exception as e:
        app.logger.error(f"Erreur lors de l'envoi du message : {str(e)}")
        return jsonify({"error": "Une erreur est survenue lors de l'envoi du message.", "details": str(e)}), 500

if __name__ == '__main__':
    # Utiliser le port dynamique pour Render
    port = int(os.environ.get("PORT", 5000))  # Utilise le port dynamique de Render ou 5000 par défaut
    app.run(host='0.0.0.0', port=port)
