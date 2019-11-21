from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, stranger"

@app.route("/<string:name>")
def hello(name):
    return render_template("index.html", name=name)

