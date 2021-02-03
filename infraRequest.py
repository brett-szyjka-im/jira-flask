import json
from jinja2 import FileSystemLoader, TemplateNotFound

env = Environment(
  loader=FileSystemLoader('/templates')
)

CPUS_KEY = 'customfield_xxxxx'
RAM_KEY = 'customfield_xxxxx'
IMAGE_KEY = ''
APPNAME_KEY = ''
ENVIRONMENT_DATA = '' # array?

# parse incoming webhook request data to extract fields we care about
def parseData(data):
	issue = json.loads(data)['issue']
	issue_id = issue['id']
  key = issue['key']
  image = issue[IMAGE_KEY]
  ram = issue[RAM_KEY]
  cpus = issue[CPUS_KEY]





# use infra_request object to template out new terraform objects
def create_pr(ir)
  tlt = env.get_template('vm.tf.jinja')
  obj = tlt.render(ir)
  return 0






class infra_request:
  """this class will contain all of the data that we want to
     pass through to terraform
  """
  key = None
  issue_id = None
  cpus = 0
  gb_ram = 0


  def __init__(self):
    
