class DynamicObject():
	def __init__(self, dictionary: dict):
		self.__dict__.update(dictionary)