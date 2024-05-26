# fastapi 
from fastapi import APIRouter, Depends, HTTPException

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.core.dependencies import get_db, oauth2_scheme 
from app.schemas.user import  FileStatus
from app.schemas.drug import CommonDto
#from app.api.endpoints.user import functions  as user_service
from app.repository import commonRepository 


router = APIRouter(
    prefix="/rpo",
    tags=["chat"]
)



# get all status
@router.get('/status',  response_model=list[FileStatus] )
async def read_all_status( db: Session = Depends(get_db)):
    return commonRepository.read_all_status(db)


# get all GetColor
@router.get('/color',  response_model=list[CommonDto] )
async def get_all_Color( db: Session = Depends(get_db)):
    return commonRepository.read_all_color(db)