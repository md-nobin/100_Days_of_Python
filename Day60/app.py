from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/templates/contact")
def contact():
    return render_template("contact.html")


@app.route("/form-entry", methods=["POST"])
def form():
    data = request.form
    print(data["name"])
    print(data["gmail"])
    print(data["phone"])
    print(data["message"])
    return " <h1> Successful </h1> "
