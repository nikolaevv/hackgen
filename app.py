from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Form, File, UploadFile, Header, status
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from main import FrontendApp, BackendApp, compress_to_archive
from schemas import AppCreatingRequestData

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.post("/api/app", response_model={})
def create_app(data: AppCreatingRequestData):
    models = [model.dict() for model in data.models]
    frontendApp = FrontendApp(data.title, data.theme, data.mainColor, data.secondaryColor, data.secondaryContrastColor, data.contrastColor, data.componentNames, [], models)
    frontendApp.generate_app()
    backendApp = BackendApp(models)
    backendApp.generate_app()
    compress_to_archive('.')
    return {}