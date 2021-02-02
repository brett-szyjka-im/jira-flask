from flask import Flask, request
app = Flask(__name__)

@app.route('/api/infrastructure-request', methods=['POST'])
def jiraEndpoint():
	request_data = request.get_json()
	print(request_data)
	return "ok"

@app.route('/api/health', methods=['GET'])
def health():
	return "healthy"
