# main.py

import os
import schedule
import time
from prepbot import PrepBot
from email_sender import EmailSender
from task_manager import TaskManager

from dotenv import load_dotenv
import json
import argparse


# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT_EMAIL") or EMAIL_ADDRESS





def parse_args():
    parser = argparse.ArgumentParser(description="PrepBot CLI")
    parser.add_argument(
        "--update",
        nargs="+",  # Allow multiple updates
        help='Update a task in format: "TaskName status" e.g., "Java done"'
    )
    return parser.parse_args()

# def update_task(self, task_name, status):
#     if task_name in self.tasks:
#         self.tasks[task_name] = status
#         self.save_tasks()
#     else:
#         print(f"⚠️ Task '{task_name}' not found. Skipped.")



# ---------------- Main ----------------
def main():
    args = parse_args()  # Get CLI arguments

    email_sender = EmailSender(EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT)
    task_manager = TaskManager()
    bot = PrepBot(email_sender, task_manager)

    # If --update is provided, update the task first
    if args.update:
        for item in args.update:   # item is like "Java done"
            try:
                task_name, status = item.split()  # split each string individually
                task_manager.update_task(task_name, status)
                print(f"✅ Task updated: {task_name} -> {status}")
            except ValueError:
                print(f"❌ Invalid format: {item}. Use: TaskName status")
        

    # Send the daily email
    
    bot.send_daily_email()
    print("📧 Morning reminder sent!")

    # --- Schedule Evening Progress Logging ---
    def evening_job():
        task_manager.save_yesterday_progress()
        print("📝 Evening progress saved!")

    # schedule.every().day.at("21:00").do(evening_job)

    # # Keep scheduler running
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)


if __name__ == "__main__":
    main()
