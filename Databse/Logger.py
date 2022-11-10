from abc import	ABC, abstractmethod

class Logger(ABC):
	@abstractmethod
	def	log(self, index_name: str, doc:	dict):
		pass