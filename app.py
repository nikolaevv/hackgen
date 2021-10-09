from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Form, File, UploadFile, Header, status
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from main import FrontendApp, BackendApp, compress_to_archive
from schemas import AppCreatingRequestData
import threading
import random
import redis
import os
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

store = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def generate_id():
    id = random.randint(0, 999999999)
    if store.get(id) is not None:
        return generate_id()
    return id

def generate_app(id, data):
    models = [model.dict() for model in data.models]
    os.makedirs('./result/{}/frontend'.format(id))
    os.makedirs('./result/{}/backend'.format(id))
    frontendApp = FrontendApp(data.title, data.theme, data.mainColor, data.secondaryColor, data.secondaryContrastColor, data.contrastColor, data.componentNames, [], models, id)
    frontendApp.generate_app()
    backendApp = BackendApp(models, id)
    backendApp.generate_app()
    compress_to_archive('.', id)
    store.set(id, 'DONE')

@app.post("/api/app", response_model={})
def create_app(data: AppCreatingRequestData):
    id = generate_id()
    store.set(id, 'PROCESSING')

    task = threading.Thread(target = generate_app, args=(id, data))
    task.start()

    return {'id': id}

@app.get("/api/app/{id}/status", response_model={})
def get_app_status(id: int):
    status = store.get(id)
    return {'status': status}

@app.get("/app/{id}/source", response_model={})
def get_source(id: int):
    status = store.get(id)
    print(status)
    if status == 'DONE':
        return FileResponse('./archives/{}.zip'.format(id))
    raise HTTPException(status_code = 403, detail = "Not proceeded")