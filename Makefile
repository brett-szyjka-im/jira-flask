tail:
	az webapp log tail --resource-group jirahook --name pythonjirahook

restart:
	az webapp restart --resource-group jirahook --name pythonjirahook

test:
	curl -X POST -H "Content-Type: text/json" -d @tests/data.json https://pythonjirahook.azurewebsites.net/api/infrastructure-request

sync:
	az webapp deployment source sync --resource-group jirahook --name pythonjirahook

build-local:
	pip3.8 install -r requirements.txt
	flask run

test-local:
	curl -X POST -H "Content-Type: text/json" -d @tests/sample.json http://localhost:5000/api/infrastructure-request
