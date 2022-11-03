import os


class tempDir():
	def __init__(self, dirName):
		self.dirName = dirName
		pass
	
	def __enter__(self):
		print('entered')
		if (not os.path.exists(self.dirName)):
			return os.mkdir(self.dirName)
		else: raise Exception('a file/dir named temp already exists!')
	
	def __exit__(self, type, value, traceback):
		print('exited')
		for root, dirs, files in os.walk(self.dirName, topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))
		os.rmdir(self.dirName)