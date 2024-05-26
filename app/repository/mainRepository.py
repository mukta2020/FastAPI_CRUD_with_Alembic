from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

# from auth import models, schemas
from passlib.context import CryptContext
from jose import JWTError, jwt

# import 
from app.models import user as UserModel
from app.schemas.user import UserCreate, UserUpdate
from app.core.settings import SECRET_KEY, ALGORITHM
from app.core.dependencies import get_db, oauth2_scheme

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



#=======================Status function=============


# get all status
def read_all_status(db: Session):
    print('hi')
    stList = db.query(UserModel.FileStatus).all()
    
    #import pdb; pdb.set_trace()
    return stList
