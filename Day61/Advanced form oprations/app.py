from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="Please enter a valid email")])
    password = PasswordField( label="Password", validators=[DataRequired(), Length(min=8, message="Password should be 8 character")])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "a;ldsfkjhajdsghfoihefkjoi"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return "success"
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)







