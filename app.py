from flask import Flask
app = Flask(__name__)

@app.route('/jira-endpoint', methods=['POST'])
def jiraEndpoint(payload):
	print(payload)

@app.route('/health', methods=['GET'])
def health():
	return "healthy"