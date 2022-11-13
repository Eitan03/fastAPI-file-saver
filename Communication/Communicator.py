from abc import	ABC, abstractmethod

class Communicator(ABC):
	@abstractmethod
	def	log(self, index_name: str, doc:	dict):
		pass