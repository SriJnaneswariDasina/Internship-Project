from flask import Flask, render_template, request
from config import db
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import logging
import os

# -----------------------------
# App Setup
# -----------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

# -----------------------------
# Create logs folder if not exists
# -----------------------------
if not os.path.exists('logs'):
    os.makedirs('logs')

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(filename='logs/events.log', level=logging.INFO)

# -----------------------------
# Database Model
# -----------------------------
class Tracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    clicked = db.Column(db.Boolean, default=False)
    submitted = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime)

# -----------------------------
# Create DB Tables
# -----------------------------
with app.app_context():
    db.create_all()

# -----------------------------
# Home Route
# -----------------------------
@app.route('/')
def home():
    return """
    <h2>Phishing Simulation Platform</h2>
    <a href='/send'>📧 Send Campaign</a><br><br>
    <a href='/dashboard'>📊 View Dashboard</a>
    """

# -----------------------------
# Phishing Page
# -----------------------------
@app.route('/phish/<email>', methods=['GET', 'POST'])
def phish(email):

    # When user clicks link
    if request.method == 'GET':
        record = Tracking(
            email=email,
            clicked=True,
            submitted=False,
            timestamp=datetime.now()
        )
        db.session.add(record)
        db.session.commit()

    # When user submits form
    if request.method == 'POST':
        record = Tracking(
            email=email,
            clicked=True,
            submitted=True,
            timestamp=datetime.now()
        )
        db.session.add(record)
        db.session.commit()

        logging.info(f"{email} submitted at {datetime.now()}")

        return "<h3>⚠️ This was a phishing simulation. Stay alert!</h3>"

    return render_template('phishing_page.html')

# -----------------------------
# Send Email Function
# -----------------------------
def send_email(target_email, link):
    sender = "dvrddvn@gmail.com"
    password = "abcd efgh ijkl mnop"

    msg = MIMEText(f"""
    <h3>Security Alert</h3>
    <p>Your account needs verification.</p>
    <a href="{link}">Click here to verify</a>
    """, "html")

    msg['Subject'] = "Important Security Update"
    msg['From'] = sender
    msg['To'] = target_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, target_email, msg.as_string())
    server.quit()

# -----------------------------
# Send Campaign
# -----------------------------
@app.route('/send')
def send_campaign():
    users = ["test@example.com"]  # Add your test emails

    for user in users:
        link = f"http://127.0.0.1:5500/phish/{user}"
        send_email(user, link)

    return "<h3>✅ Emails Sent Successfully!</h3>"

# -----------------------------
# Dashboard
# -----------------------------
@app.route('/dashboard')
def dashboard():
    data = Tracking.query.all()

    total = len(data)
    clicks = sum(1 for d in data if d.clicked)
    submitted = sum(1 for d in data if d.submitted)

    return render_template(
        "dashboard.html",
        total=total,
        clicks=clicks,
        submitted=submitted
    )

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)