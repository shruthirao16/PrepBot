# day1_send_test_email.py
import os
import ssl
import smtplib
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv

# Load .env
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT_EMAIL") or EMAIL_ADDRESS

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise SystemExit("Please set EMAIL_ADDRESS and EMAIL_APP_PASSWORD in .env")

def make_message(subject: str, plain_text: str, html: str = None) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT
    msg["Subject"] = subject
    msg.set_content(plain_text)
    if html:
        msg.add_alternative(html, subtype="html")
    return msg

def send_email(msg: EmailMessage):
    smtp_host = "smtp.gmail.com"
    smtp_port = 465  # SSL port
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    subject = f"Prep Guardian — Test Email ({today})"
    plain = (
        "Hey Shruthi!\n\n"
        "This is a test email from your Prep Guardian Bot.\n\n"
        "Tasks (example):\n"
        "- Java: pending\n"
        "- DSA: pending\n"
        "- AWS: pending\n\n"
        "If you got this, the bot works! 🎉\n"
    )
    html = f"""
    <html>
      <body>
        <h2>Prep Guardian — Test Email</h2>
        <p>Hi Shruthi 👋 — this is a test message from your Prep Guardian Bot.</p>
        <ul>
          <li><b>Java:</b> pending</li>
          <li><b>DSA:</b> pending</li>
          <li><b>AWS:</b> pending</li>
        </ul>
        <p><i>Sent at {today}</i></p>
        <p>🎉 If you received this, Day 1 is a success!</p>
      </body>
    </html>
    """
    msg = make_message(subject, plain, html)
    send_email(msg)
    print("Email sent — check your inbox (and spam).")

if __name__ == "__main__":
    main()
