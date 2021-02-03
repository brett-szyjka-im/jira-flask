# flask-based web app for jira webhook infrastructure automation

## pre-requisites
- python 3.8 / pip
	- code dependencies are installed via 'pip3.8 install -r requirements.txt' command

### optional

- az cli
	- used in makefile scripts

## ci
- this app is set to deploy via CI to https://pythonjirahook.azurewebsites.net/ from the _main_ branch

## endpoints
- /api/health
	- healthcheck endpoint, returns string "healthy"
- /api/infrastructure-request
	- this endpoint is reached by the webhook installed on jira

## fields we care about (this'll be expanded after POC)
- issue id / issue key
  - this is important for auditability / context with the generated PR
- appname
  - this is used to construct the dynamic hostnames of machines generated by tf
- image / os selection
  - from dropdown, we can also decide which images we can automatically deploy and which are likely to require intervention
- cpus
  - self-explanatory
  - along with other quantitative 'spec' fields, we want to qualify these fields with limits
- ram
  - as above
- specified environments
  - checkboxes or similar for each environment (dev, qa, stage, prod, genesys)
- for each environment: number of servers
  - e.g. prod-4, stage-3
- networking information?
- role? (app vs web)

## atlassian-jira details
- [jira url](https://jiratestszyjka.atlassian.net)
- [project url](https://jiratestszyjka.atlassian.net/jira/servicedesk/projects/IR)
- webhook name: 

### custom fields
#### prefix for all of our custom fields: ir_
- ir_appname
- ir_image
- ir_cpus
  - the 'cpus' value represents the number of virtual compute cores that will be assigned to each provisioned vm
  - NOTE: jira doesn't seem to like the value '>8' in it's dropdown list for this field. possibly starting with a symbol?
- ir_ram
  - MB
  - the 'ram' value represents the amount of memory that will be assigned to each provisioned vm 
- ir_environments
  - the 'environments' value represents each environment that the requested vm cluster will be deployed to
  - to make it easier for now, we're going to create the same number of machines in each environment. I'm aware that this will probably have to change
  - another assumption that I'm making to speed things up is that the datacenter can be determined by the provided environment value (prod/stage=WJ, qa/dev=TX). I'm aware that this is going to change because that's one of our current concerns
- ir_role
  - the 'role' value represents the server's role in the IM infrastructure. e.g. app, web, sql, etc
- ir_nodes
  - the 'nodes' value represents the number of servers to be deployed to each environment

### field configuration
- infra-req_field_configuration
  - 

### screens
- intra-req_screen
- infra-req_screen_scheme

### issue_type
- [Infra] Red Request
- infra-req_issue_type_screen_scheme
- infra-req_issue_type_scheme
