import yaml
import json

server = {
"server": "prod", 
"port": 80, 
"status": "active"
}

with open('config.json', 'w') as json_file:
	json.dump(server, json_file, indent=4)

with open('config.json', 'r') as json_file:
	json_data = json.load(json_file)
	
json_data['status'] = "maintenance"
with open('config.yaml', 'w') as yaml_file:
	yaml.dump(json_data, yaml_file)