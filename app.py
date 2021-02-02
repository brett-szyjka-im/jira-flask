from flask import Flask, request
import infraRequest
app = Flask(__name__)

@app.route('/api/infrastructure-request', methods=['POST'])
def jiraEndpoint():
	request_data = request.get()
	print(infraRequest.parseData(request_data))

@app.route('/api/health', methods=['GET'])
def health():
	return "healthy"
