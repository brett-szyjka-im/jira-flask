from flask import Flask, request
import infraRequest
app = Flask(__name__)

@app.route('/api/infrastructure-request', methods=['POST'])
def jiraEndpoint():
	request_data = request.get_data(as_text=True)
	print('request id to follow:')
	print(infraRequest.parseData(request_data))
	return "ok"

@app.route('/api/health', methods=['GET'])
def health():
	return "healthy"
