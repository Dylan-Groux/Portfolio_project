from flask import jsonify, request, Flask
from . import app, mail
from flask_mail import Message
import logging

logging.basicConfig(level=logging.DEBUG)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    app.logger.debug(f'Requête reçue: {data}') #Affiche les données envoyés du front-end (debug)
    
    if not data:
        return jsonify({'error': 'Aucune donnée reçue'}), 400        

    # Vérification des champs requis
    required_fields = ['name', 'email', 'phone', 'message', 'sujet']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Le champ {field} est requis."}), 400

    name = data['name']
    email = data['email']
    phone = data['phone']
    sujet = data['sujet']
    message_content = data['message']

    # Création du message
    subject = f"Nouveau message de contact de {name}"
    body = f"Nom: {name}\nEmail: {email}\nTéléphone: {phone}\n\nMessage:\n{message_content}\n Sujet : {sujet}"

    try:
        msg = Message(subject, sender=email, recipients=['smtpredar@gmail.com'])
        msg.body = body
        mail.send(msg)
        return jsonify({"success": "Message envoyé avec succès."}), 200
    except Exception as e:
        app.logger.error(f"Erreur lors de l'envoi du message : {str(e)}") # Récupère plus précisement l'erreur (debug)
        return jsonify({"error": "Une erreur est survenue lors de l'envoi du message.", "details": str(e)}), 500
