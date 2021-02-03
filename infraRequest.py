import json

def parseData(data):
	issue = json.loads(data)
	id = issue['issue']['id']
	return id
