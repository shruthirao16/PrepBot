# PrepBot
PrepBot (a.k.a PrepBuddy) 🤖🎓

PrepBot is your personal study companion bot that helps you stay on track with your daily preparation.
It automatically sends you reminder emails about your tasks (Java, DSA, AWS, etc.) so you never lose focus.

✨ Features

📧 Sends automatic daily reminder emails

🔒 Uses secure Gmail App Passwords with .env

📝 Customizable task list and email content

⏰ Will support scheduling (daily/weekly reminders)

🎨 Both plain-text & HTML email formats

⚙️ Tech Stack

Python 3.9+

smtplib (for email)

dotenv (for credentials)

schedule (for future daily automation)

🚀 Getting Started
1. Clone the repo
git clone https://github.com/your-username/PrepBot.git
cd PrepBot

2. Set up virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

3. Install dependencies
pip install -r requirements.txt

4. Add .env file

Create a .env in the project root:

EMAIL_ADDRESS=your_email@gmail.com  
EMAIL_APP_PASSWORD=your_gmail_app_password  
RECIPIENT_EMAIL=recipient_email@gmail.com  

5. Run the bot
python day1_send_test_email.py


🛠 Future Plans

Add a task tracker file (JSON/CSV)

Enable daily auto-scheduling

Add progress tracking & streaks

(Optional) Telegram/WhatsApp notifications

🤝 Contributing

This is a personal project but feel free to fork and experiment!
