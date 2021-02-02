import json

def parseData(data):
	issue = json.loads(data)
	id = issue['issue'][0]['id']
	return id
