import socket
import json

config = None
with open('config.json', 'r') as f:
	config = json.load(f)

config['MY_IP'] = socket.gethostbyname(socket.gethostname())