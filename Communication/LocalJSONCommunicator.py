from datetime import datetime
import json
import logging
import os

from Communication.Communicator import Communicator

logger = logging.getLogger('')

class LocalJSONCommunicator(Communicator):
	def	__init__(self, baseDir):
		self.base_dir = baseDir

	def	log(self, index_name: str, doc: dict, add_timestamp=True):
		if add_timestamp: doc['@timestamp'] = str(datetime.now()).replace(' ', 'T') + 'Z'

		folder = os.path.join(self.base_dir,index_name)

		if not os.path.exists(folder):
			logger.info(f'creating folder {folder}')
			os.mkdir(folder)
		with open(os.path.join(folder, f'{index_name} - {datetime.now().strftime("%Y-%m-%d:%H")}.json'), 'a') as f:
			data = json.dumps(doc)
			f.write(data + '\n')
		logger.info(f'logged to elastic in index {index_name}')
