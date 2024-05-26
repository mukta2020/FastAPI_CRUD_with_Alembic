from fastapi import HTTPException, status, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Annotated
from sqlalchemy.orm import Session
from  app.repository import common
# import 
from app.schemas import drug
from app.models import user as UserModel
from typing import Any, Optional

#=======================Status function=============
class MessageHelperDto:
    message: Optional[str] = None
    data: Optional[Any] = None
    status_code: int = 0
    succeed: bool = False

# get all status
def read_all_status(db: Session):
    print('hi')
    stList = db.query(UserModel.FileStatus).all()    
    #import pdb; pdb.set_trace()
    return stList


# get all color
def read_all_color(db: Session):
    print('hi')
    # Example usage:
    function_name = "public.fn_get_drug_color_list"
    dropdown_data =common.get_dropdown_common_dto(function_name) 
    
    message_helper = MessageHelperDto()
    message_helper.data = dropdown_data
    message_helper.status_code = 200
    message_helper.succeed = True

    #import pdb; pdb.set_trace()
    return message_helper


# get all color
def read_all_color(db: Session):
    print('hi')
    # Example usage:
    function_name = "public.fn_get_drug_color_list"
    dropdown_data =common.get_dropdown_common_dto(function_name) 
    
    #import pdb; pdb.set_trace()
    return dropdown_data