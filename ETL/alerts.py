# etl/alerts.py
import smtplib
from email.mime.text import MIMEText
from config import email_config

def send_email(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = email_config["sender"]
    msg["To"] = email_config["receiver"]

    try:
        with smtplib.SMTP(email_config["smtp_server"], email_config["port"]) as server:
            server.starttls()
            server.login(email_config["sender"], email_config["password"])
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")
