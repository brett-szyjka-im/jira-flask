from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

@app.route("/jira-hook")
def hellojira():
	return "Jira Hook endpoint"
