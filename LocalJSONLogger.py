from datetime import datetime
import json
import os

class LocalJSONLogger():
	def	__init__(self, baseDir):
		self.base_dir = baseDir

	def	log(self, index_name: str, doc: dict, add_timestamp=True):
		if add_timestamp: doc['@timestamp'] = str(datetime.now()).replace(' ', 'T') + 'Z'

		folder = os.path.join(self.base_dir,index_name)

		if not os.path.exists(folder):
			print(f'creating folder {folder}')
			os.mkdir(folder)
		with open(os.path.join(folder, f'{index_name}-{str(datetime.now())}.json'), 'a') as f:
			data = json.dumps(doc)
			f.write(data + '\n')
		print(f'logged to elastic in index {index_name}')
