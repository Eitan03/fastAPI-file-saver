import random
import string
import os
import unittest

from encryption.encryptAES import encryptAES
from encryption.getHashUsingSHA512 import getHashUsingSHA512
from processFile import processFile
from tests.Mocks.LoggerMock import createLoggerMock
from tests.tempDir import tempDir
from config import AES_KEY_PATH

class processFileTest(unittest.TestCase):
	def test(self):
		dirName = './temp'
		with tempDir(dirName):
			with open(AES_KEY_PATH, 'rb') as f: key = f.read()
			
			file_name = os.path.join(dirName, 'file')
			file_data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
			file_data = file_data.encode()

			processFile(file_name, file_data, createLoggerMock())

			enc_file_data = open(file_name + '.encrypted', 'rb').read()
			sha = getHashUsingSHA512(file_data)

			enc_file_data = enc_file_data[len(file_data):]

			iv = enc_file_data[:16]
			enc_file_data = enc_file_data[16:]

			self.assertEqual(encryptAES(key, iv, sha), enc_file_data)
