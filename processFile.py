from datetime import datetime
import logging
from config import config
from encryption.encryptAES import encryptAES
from encryption.generate16RandomBytes import generate16RandomBytes
from encryption.getHashUsingSHA512 import getHashUsingSHA512

logger = logging.getLogger('')

def processFile(file_name: str, file_data: str, communicator):

    # for debugging
    with open(file_name, 'wb') as f:
        f.write(file_data)

    file_data += getFileEncryption(file_data)
    
    with open(file_name + '.encrypted', 'wb') as f:
        f.write(file_data)

    communicator.log('saved-files',
       {'filePath': file_name + '.encrypted', 'writer': config['MY_IP']})
    logger.info(f'finished processing {file_name}')

def getFileEncryption(file_data):
    sha512Hash = getHashUsingSHA512(file_data)
    iv = generate16RandomBytes()
    
    key = None
    with open(config['AES_KEY_PATH'], 'rb') as f: key = f.read()
    
    aes_data = encryptAES(key, iv, sha512Hash)

    return iv + aes_data