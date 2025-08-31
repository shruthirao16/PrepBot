import os
import json
from datetime import datetime, timedelta

class TaskManager:
    def __init__(self, filepath="data/progress.json"):
        self.filepath = filepath
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {"tasks": {}, "planned_for_today": [], "history": []}

    def save_tasks(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_tasks(self):
        return self.data["tasks", {}]

    def set_task_status(self, task, status="pending"):
        if task in self.data.get("tasks", {}):
            self.data["tasks"][task] = status
            self.save_tasks()

    def set_planned_for_today(self, tasks):
        self.data["planned_for_today"] = tasks
        self.save_tasks()

    def save_yesterday_progress(self):
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        # completed = [t for t, done in self.data["tasks"].items() if done]
        # pending = [t for t, done in self.data["tasks"].items() if not done]

        self.data["history",[]].append({
            "date": yesterday,
            "updates": self.data.get("tasks", {}).copy()
            # "completed": completed,
            # "pending": pending
        })
        self.save_tasks()
        print(f"📝 Progress saved for {yesterday}.")

    def get_yesterday_summary(self):
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        for record in reversed(self.data["history"]):
            if record["date"] == yesterday:
                return record["updates"]
        return {}

    def get_today_plan(self):
        return self.data.get("planned_for_today", list(self.data["tasks"].keys()))
    
    def all_tasks_done(self):
        return all(status for status in self.get_tasks().values())