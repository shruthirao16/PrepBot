from task_manager import TaskManager
from email_sender import EmailSender  # your existing EmailSender

class PrepBot:
    def __init__(self, email_sender, task_manager):
        self.task_manager = task_manager
        self.email_sender = email_sender

    def send_daily_email(self):
        yesterday_updates = self.task_manager.get_yesterday_summary()
        today_plan = self.task_manager.get_today_plan()

        all_done = all("done" in status.lower() for status in yesterday_updates.values())

        html = "<h2>Good Morning!</h2>"

        if all_done:
            html += "<h3>🎉 All tasks are completed!</h3>"

        # Yesterday's summary
        html += "<h3>Yesterday's Progress:</h3><ul>"
        for task, status in yesterday_updates.items():
            color = "green" if "done" in status.lower() else "orange"
            html += f"<li style='color:{color}'>{task} - {status}</li>"
        html += "</ul>"

        # Today's plan
        html += "<h3>Today's Plan:</h3><ul>"
        for t in today_plan:
            html += f"<li style='color:blue'>{t}</li>"
        html += "</ul>"

        html += "<p>Any updates or changes for today?</p>"

        self.email_sender.send_email(
            subject="Your Thoughtful PrepBuddy Morning Reminder",
            plain_text="Here is your daily reminder.",  # required
            html=html
        )
