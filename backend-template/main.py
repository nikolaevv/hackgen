from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Form, File, UploadFile, Header, status
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import SessionLocal, engine
import smtplib

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
) 

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def authorize(token: str, model, role: str = 'ALL', id: int = None, db: Session = Depends(get_db)) -> bool:
    if token:
        access_token = token.split('Bearer ')[-1]
        suitable_users = db.query(models.User).filter(model.access_token == access_token)
        if suitable_users.count() > 0:
            suitable_user = suitable_users.first()
            if (role == 'ALL' or suitable_user.role.value == role) or (suitable_user.business_id == id):
                return suitable_user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def authorize_user(token: str, model, role: str = 'ALL', id: int = None, db: Session = Depends(get_db)) -> bool:
    return authorize(token, db, model, role, id)

