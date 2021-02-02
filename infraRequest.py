import json

def parseData(data):
	json = json.loads(data)
	id = json['issue'][0]['id']
	return id
