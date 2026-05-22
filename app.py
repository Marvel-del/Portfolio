from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)


# HOME
@app.route("/")
def home():
    return render_template("index.html")


# ABOUT
@app.route("/about")
def about():
    return render_template("about.html")


# CONTACT
@app.route("/contact")
def contact():
    return render_template("contact.html")


# SEND MESSAGE
@app.route("/send", methods=["POST"])
def send():

    name    = request.form["name"]
    email   = request.form["email"]
    message = request.form["message"]

    try:

        # Load credentials from environment variables (never hard-code passwords)
        sender_email    = os.environ.get("GMAIL_ADDRESS", "marvellousakachukwu@gmail.com")
        sender_password = os.environ.get("GMAIL_APP_PASSWORD")

        msg = MIMEText(f"""
New portfolio contact form submission
--------------------------------------
Name:    {name}
Email:   {email}

Message:
{message}
--------------------------------------
""")

        msg["Subject"]  = f"Portfolio Contact: {name}"
        msg["From"]     = sender_email
        msg["To"]       = sender_email
        msg["Reply-To"] = email   # reply directly to the visitor

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return "Message Sent Successfully!"

    except Exception as e:
        return f"Error: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
