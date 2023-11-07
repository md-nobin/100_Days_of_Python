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
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", meg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"subject: New message \n \n {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(os.getenv("my_gmail"), os.getenv("password"))

    server.sendmail(os.getenv("my_gmail"), os.getenv("my_gmail"), email_message)



