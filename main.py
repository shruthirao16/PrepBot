# main.py

import os
import ssl
import smtplib
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT_EMAIL") or EMAIL_ADDRESS


# ---------------- Email Sender ----------------
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
        msg = self.make_message(subject, plain_text, html)
        smtp_host = "smtp.gmail.com"
        smtp_port = 465
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
            server.login(self.email_address, self.email_password)
            server.send_message(msg)
        print("✅ Email sent successfully!")


# ---------------- Task Manager ----------------
class TaskManager:
    def __init__(self, task_file="data/progress.json"):
        self.task_file = task_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.task_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"Java": "pending", "DSA": "pending", "AWS": "pending"}

    def save_tasks(self):
        with open(self.task_file, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def update_task(self, task_name, status):
        if task_name in self.tasks:
            self.tasks[task_name] = status
            self.save_tasks()


# ---------------- PrepBot Controller ----------------
class PrepBot:
    def __init__(self, email_sender: EmailSender, task_manager: TaskManager):
        self.email_sender = email_sender
        self.task_manager = task_manager

    def send_daily_reminder(self):
        today = datetime.now().strftime("%Y-%m-%d %H:%M")
        subject = f"PrepBuddy — Daily Reminder ({today})"

        # Construct email content
        plain = "Hey Shruthi! Here are your tasks for today:\n\n"
        html = "<html><body><h2>PrepBuddy — Daily Reminder</h2><ul>"

        for task, status in self.task_manager.tasks.items():
            plain += f"- {task}: {status}\n"
            html += f"<li><b>{task}:</b> {status}</li>"

        plain += "\n🎉 Keep going, you got this!"
        html += f"</ul><p><i>Sent at {today}</i></p></body></html>"

        self.email_sender.send_email(subject, plain, html)


# ---------------- Main ----------------
def main():
    email_sender = EmailSender(EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT)
    task_manager = TaskManager()
    bot = PrepBot(email_sender, task_manager)

    bot.send_daily_reminder()


if __name__ == "__main__":
    main()
