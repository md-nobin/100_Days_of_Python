from flask import Flask
from flask import render_template
from flask import request
from dotenv import load_dotenv
import os
import smtplib
import ssl
from email.message import EmailMessage
load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/post")
def post():
    return render_template("/post.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(os.getenv("my_gmail"), os.getenv("password"))
        connection.sendmail(os.getenv("my_gmail"), os.getenv("my_gmail"), email_message)
