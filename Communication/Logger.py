import logging
from logging.handlers import TimedRotatingFileHandler

from config import config

def initLogger():
	log = logging.getLogger('')
	log.setLevel(logging.DEBUG)

	jsonFormatter = logging.Formatter(
		'{ \"@timestamp\": \"%(asctime)s\", \"level\": \"%(levelname)s\", \"message\": \"%(message)s\"' + 
			', \"sender\": \"' + config['MY_IP'] + '\" }'
		, datefmt='%Y-%m-%dT%H:%M:%SZ'
		) 

	fh = TimedRotatingFileHandler('elasticLogs/errors/errors.json', when='H', interval=3, encoding='utf-8')
	fh.setLevel(logging.WARNING)
	fh.setFormatter(jsonFormatter)
	log.addHandler(fh)


	consoleFormatter = logging.Formatter('[%(levelname)s] - %(message)s')
	ch = logging.StreamHandler()
	ch.setLevel(logging.INFO)
	ch.setFormatter(consoleFormatter)
	log.addHandler(ch)