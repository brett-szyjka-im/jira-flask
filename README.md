# Flask-based Jira Webhook for Infrastructure Automation

## CI
- this app is set to deploy via CI to https://pythonjirahook.azurewebsites.net/ from the _main_ branch

## Endpoints
- /api/health
	- healthcheck endpoint, returns string "healthy"
- /api/infrastructure-request
	- this endpoint is reached by the webhook installed on jira
