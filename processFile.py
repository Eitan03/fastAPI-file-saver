from datetime import datetime
from config import AES_KEY_PATH, MY_IP
from encryption.encryptAES import encryptAES
from encryption.generate16RandomBytes import generate16RandomBytes
from encryption.getHashUsingSHA512 import getHashUsingSHA512

def processFile(file_name: str, file_data: str, logger):

    # for debugging
    with open(file_name, 'wb') as f:
        f.write(file_data)

    sha512Hash = getHashUsingSHA512(file_data)
    iv = generate16RandomBytes()
    
    key = None
    with open(AES_KEY_PATH, 'rb') as f: key = f.read()
    
    aes_data = encryptAES(key, iv, sha512Hash)

    file_data += iv
    file_data += aes_data
    
    with open(file_name + '.encrypted', 'wb') as f:
        f.write(file_data)

    logger.log('saved-files',
       {'filePath': file_name + '.encrypted', 'writer': MY_IP})
    print(f'finished processing {file_name}')