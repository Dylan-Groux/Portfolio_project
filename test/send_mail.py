import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration de l'expéditeur et du destinataire
email_sender = "smtpredar@gmail.com"
email_password = "cvgl yoab izyi rvws" 
email_recipient = "smtpredar@gmail.com"

# Création du message
subject = "Test depuis Python"
body = "Ceci est un message envoyé depuis Python pour tester la configuration."

message = MIMEMultipart()
message["From"] = email_sender
message["To"] = email_recipient
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Affichage des informations pour débogage
print("[DEBUG] Détails de l'e-mail :")
print(f"Expéditeur : {email_sender}")
print(f"Destinataire : {email_recipient}")
print(f"Sujet : {subject}")
print(f"Corps : {body}")

try:
    # Connexion au serveur SMTP de Gmail
    print("[INFO] Connexion au serveur SMTP...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.set_debuglevel(1)  # Active le mode débogage pour afficher les détails SMTP
    server.starttls()  # Sécurisation de la connexion
    print("[INFO] Authentification...")
    server.login(email_sender, email_password)  # Authentification

    # Envoi de l'e-mail
    print("[INFO] Envoi de l'e-mail...")
    server.sendmail(email_sender, email_recipient, message.as_string())
    print("[SUCCÈS] E-mail envoyé avec succès !")

    # Déconnexion
    server.quit()
except Exception as e:
    print(f"[ERREUR] Une erreur s'est produite : {e}")
