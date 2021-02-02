tail:
	az webapp log tail --resource-group jirahook --name pythonjirahook

restart:
	az webapp restart --resource-group jirahook --name pythonjirahook

test:
	curl -X POST -H "Content-Type: text/json" @data.json https://pythonjirahook.azurewebsites.net/api/infrastructure-request
