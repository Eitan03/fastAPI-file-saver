from Crypto.Hash import SHA512

def getHashUsingSHA512(file_data: str):
    hash = SHA512.new(data=file_data)
    return hash.digest()