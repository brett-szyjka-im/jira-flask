from flask import Flask, request
app = Flask(__name__)

@app.route('/jira-endpoint', methods=['POST'])
def jiraEndpoint():
	request_data = request.get_json()
	data = request_data['payload']
	print(data)

@app.route('/health', methods=['GET'])
def health():
	return "healthy"
