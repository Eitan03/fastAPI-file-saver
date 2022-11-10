import random
import string
import os
import unittest
from unittest.mock import ANY, Mock

from encryption.encryptAES import encryptAES
from encryption.getHashUsingSHA512 import getHashUsingSHA512
from processFile import processFile
from tests.Mocks.CommunicatorMock import createCommunicatorMock
from tests.TempDir import TempDir
from config import AES_KEY_PATH, MY_IP

class processFileTest(unittest.TestCase):
	def test_processFile_adds_encryption_to_end_of_file(self):
		dirName = './temp'
		with TempDir(dirName):
			with open(AES_KEY_PATH, 'rb') as f: key = f.read()
			
			file_name = os.path.join(dirName, 'file')
			file_data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100)).encode()

			processFile(file_name, file_data, createCommunicatorMock())

			enc_file_data = open(file_name + '.encrypted', 'rb').read()
			sha = getHashUsingSHA512(file_data)

			enc_file_data = enc_file_data[len(file_data):]

			iv = enc_file_data[:16]
			enc_file_data = enc_file_data[16:]

			self.assertEqual(encryptAES(key, iv, sha), enc_file_data)
		
	def test_processFile_log(self):
		dirName = './temp'
		with TempDir(dirName):
			with open(AES_KEY_PATH, 'rb') as f: key = f.read()
			
			file_name = os.path.join(dirName, 'file')
			file_data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100)).encode()


			communicator =Mock(return_value=True)

			processFile(file_name, file_data, createCommunicatorMock({ 'log': communicator }))

			communicator.assert_called_once_with('saved-files', {'filePath': file_name + '.encrypted', 'writer': MY_IP})