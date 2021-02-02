from flask import Flask
import requests
app = Flask(__name__)

@app.route('/jira-endpoint', methods=['POST'])
def jiraEndpoint(self):
	request_data = request.get_json()
	data = request_data['payload']
	print(data)

@app.route('/health', methods=['GET'])
def health():
	return "healthy"
