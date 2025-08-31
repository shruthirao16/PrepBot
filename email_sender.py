import ssl
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta

class EmailSender:
    def __init__(self, email_address, email_password, recipient):
        self.email_address = email_address
        self.email_password = email_password
        self.recipient = recipient

    def make_message(self, subject: str, plain_text: str, html: str = None) -> EmailMessage:
        msg = EmailMessage()
        msg["From"] = self.email_address
        msg["To"] = self.recipient
        msg["Subject"] = subject
        msg.set_content(plain_text)
        if html:
            msg.add_alternative(html, subtype="html")
        return msg

    def send_email(self, subject: str, plain_text: str, html: str = None):
        try:
            msg = self.make_message(subject, plain_text, html)
            smtp_host = "smtp.gmail.com"
            smtp_port = 465
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
                server.login(self.email_address, self.email_password)
                server.send_message(msg)
            print("✅ Email sent successfully!")
        except Exception as e:
            print("❌ Failed to send email:", e)

    
