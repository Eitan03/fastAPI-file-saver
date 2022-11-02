from Crypto.Cipher import AES

def encryptAES(key, iv, data):
    chiper = AES.new(key, AES.MODE_CFB, iv=iv)
    chipered_bytes = chiper.encrypt(data)
    return chipered_bytes