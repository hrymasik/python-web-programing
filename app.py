from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route('/maksym')
def maksym():
    return "Hello, Maksym!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"