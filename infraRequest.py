import yaml
import json
from jinja2 import FileSystemLoader, TemplateNotFound, Environment

env = Environment(
  loader=FileSystemLoader('/templates')
)

CUSTOMFIELD_PREFIX = 'customfield'
cfg = None

def loadConfig():
	with open('jirafieldconfig.yaml') as f:
		cfg = yaml.load(f, Loader=yaml.FullLoader)

# parse incoming webhook request data to extract fields we care about
def parseData(data):
	loadConfig()
	ir = infrareq(json.loads(data))
	print_request_summary(ir)

# use infrareq object to template out new terraform objects
# def create_pr(ir)
#   tlt = env.get_template('vm.tf.jinja')
#   obj = tlt.render(ir)
#   return 0

def print_request_summary(ir_obj):
	for attr, value in ir_obj.__dict__.items():
		print(attr, value)
	return

class infrareq:
  def __init__(self, json_data):
  	ir = json_data['issue']['fields']
  	PRE = CUSTOMFIELD_PREFIX
  	initialize(
  			ir['id'] #issue_id
  		, ir[f"{PRE}_{cfg.appname.key}"] #appname
  		, ir[f"{PRE}_{cfg.role.role}"] #role
  		, ir[f"{PRE}_{cfg.image.key}"] #image
  		, ir[f"{PRE}_{cfg.env.key}"] #env
  		, ir[f"{PRE}_{cfg.nodes.key}"] #nodes
  		, ir[f"{PRE}_{cfg.cpus.key}"] #cpus
  		, ir[f"{PRE}_{cfg.gb_ram.key}"] #gb_ram
  		, ir[f"{PRE}_{cfg.gb_disk.key}"] #gb_disk
  		, ir[f"{PRE}_{cfg.network.key}"] #network
		)

  def initialize(key, issue_id, appname, role, image, env, nodes, cpus, gb_ram, gb_disk, network):
  	self.key = key
  	self.issue_id = issue_id
  	self.appname = appname
  	self.role = role
  	self.image = image
  	self.env = env
  	self.nodes = nodes
  	self.cpus = cpus
  	self.gb_ram = gb_ram
  	self.gb_disk = disk
  	self.network = network
