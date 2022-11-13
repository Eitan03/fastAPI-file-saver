from config import config
from encryption.encryptAES import encryptAES
from encryption.generate16RandomBytes import generate16RandomBytes
from encryption.getHashUsingSHA512 import getHashUsingSHA512

def encryptFile(file_data):
    sha512Hash = getHashUsingSHA512(file_data)
    iv = generate16RandomBytes()
    
    key = None
    with open(config['AES_KEY_PATH'], 'rb') as f: key = f.read()
    
    aes_data = encryptAES(key, iv, sha512Hash)

    return file_data + iv + aes_data