import logging
from typing import List

import traceback

from fastapi import FastAPI, File, status, Form
from fastapi.responses import ORJSONResponse

from os import path
from Communication.Logger import initLogger

from config import AMOUNT_OF_FILE_PARTS, ELASTIC_HOST, IMAGES_PATH, JSON_LOGS_PATH
from Communication.LocalJSONCommunicator import LocalJSONCommunicator
from processFile import processFile

app = FastAPI()
initLogger()
logger = logging.getLogger('')


@app.head("/")
@app.get("/")
def root():
    return {"message": "Hello from fastAPI1"}

@app.post("/uploadfiles/", status_code=status.HTTP_201_CREATED, response_class=ORJSONResponse)
def create_upload_files(fileParts: List[bytes] = File(...), fileName: str = Form(...)):
    try:
        logger.info(f'recived {fileName} with {len(fileParts)} parts')

        if (len(fileParts) != AMOUNT_OF_FILE_PARTS):
            raise Exception("Invalid number of file parts where given!")

        processFile(path.join(IMAGES_PATH, fileName), b''.join(fileParts), LocalJSONCommunicator(JSON_LOGS_PATH))

    except Exception as e:

        logger.error(f'got an error! {e}')
        logger.info(f'got an error! {e}', exc_info=True)

        return ORJSONResponse({ "error": str(e) }, status.HTTP_500_INTERNAL_SERVER_ERROR)
