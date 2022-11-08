from typing import List

import traceback

from fastapi import FastAPI, File, status, Form
from fastapi.responses import ORJSONResponse

from os import path

from config import AMOUNT_OF_FILE_PARTS, ELASTIC_HOST, IMAGES_PATH
from LocalJSONLogger import LocalJSONLogger
from processFile import processFile

app = FastAPI()


@app.head("/")
@app.get("/")
async def root():
    return {"message": "Hello from fastAPI1"}

@app.post("/uploadfiles/", status_code=status.HTTP_201_CREATED, response_class=ORJSONResponse)
async def create_upload_files(fileParts: List[bytes] = File(...), fileName: str = Form(...)):
    try:
        print(f' recived {fileName} with {len(fileParts)} parts')

        if (len(fileParts) != AMOUNT_OF_FILE_PARTS):
            raise Exception("Invalid number of file parts where given!")

        processFile(path.join(IMAGES_PATH, fileName), b''.join(fileParts), LocalJSONLogger())

    except Exception as e:

        traceback.print_exc()

        return ORJSONResponse({ "error": str(e) }, status.HTTP_500_INTERNAL_SERVER_ERROR)
