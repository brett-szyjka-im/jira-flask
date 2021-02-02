from flask import Flask
app = Flask(__name__)

@app.route('/jira-endpoint', methods=['POST'])
def jiraEndpoint(payload):
	print(payload)
