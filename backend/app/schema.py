from pydantic import BaseModel,validator
from datetime import date
from app.model.person import Sex
from fastapi import HTTPException
from typing import Optional,TypeVar,Generic,List
from pydantic.generics import GenericModel


T = TypeVar('T')

class PersonCreate(BaseModel):
    name:str
    sex:Sex
    birth_date: date
    birth_place:str
    country:str


    #sex validation 
    @validator("sex")
    def sex_validation(cls,v):
        if hasattr(Sex, v) is False:
            raise HTTPException(status_code=400,detail="Invalid input sex")
        return v



class ResponseSchema(BaseModel):
    detail:str
    result:Optional[T]= None


class PageResponse(GenericModel,Generic[T]):
    """"The response for a pagination query."""

    page_number:int
    page_size:int
    total_pages:int
    total_record:int    
    content:List[T]
                   


