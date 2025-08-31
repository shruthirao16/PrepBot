import os
from dotenv import load_dotenv
from email_sender import EmailSender

# Load .env variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT_EMAIL") or EMAIL_ADDRESS

# Create EmailSender instance
sender = EmailSender(EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT)

# Send a test email immediately
sender.send_email(
    subject="PrepBot Immediate Test",
    plain_text="This is a test email sent immediately from PrepBot.",
    html="<h1>PrepBot Immediate Test</h1>"
)
