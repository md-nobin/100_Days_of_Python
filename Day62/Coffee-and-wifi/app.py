from flask import Flask, render_template, request
import flask_bootstrap

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shop-list")
def shop_list ():
    return render_template("shop-list.html")


@app.route("/add-shop")
def add_shop():
    return render_template("add-shop.html")
