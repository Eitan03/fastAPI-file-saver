from datetime import datetime
import logging
from config import config
from encryptFile import encryptFile

logger = logging.getLogger('')

def processFile(file_name: str, file_data: str, communicator):

    # for debugging
    with open(file_name, 'wb') as f:
        f.write(file_data)

    file_data = encryptFile(file_data)
    
    with open(file_name + '.encrypted', 'wb') as f:
        f.write(file_data)

    communicator.log('saved-files',
       {'filePath': file_name + '.encrypted', 'writer': config['MY_IP']})
    logger.info(f'finished processing {file_name}')
