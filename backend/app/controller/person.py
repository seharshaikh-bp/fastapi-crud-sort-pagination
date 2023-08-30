from fastapi import APIRouter,Path,Query
from app.schema import ResponseSchema,PersonCreate
from app.repository.person  import PersonRepository


router =APIRouter(
    prefix="/person",
    tags=['person']
)


@router.post("",response_model=ResponseSchema,response_model_exclude_none=True)
async def create_person(create_form:PersonCreate):
    await PersonRepository.create(create_form)
    return ResponseSchema(detail="successfully created data!")  


@router.patch("/{id}",response_model=ResponseSchema,response_model_exclude_none=True)
async def update_person(
         person_id:int = Path(...,alias="id"),
         *,
         update_form:PersonCreate

):
    await PersonRepository.update(person_id,update_form)
    return ResponseSchema(detail="successfully updated date!")


@router.delete("/{id}",response_model=ResponseSchema,response_model_exclude_none=True)
async def delete_person(
          person_id:int = Path(...,alias="id")
):
    await PersonRepository.delete(person_id)
    return ResponseSchema(detail="successfully deleted data!")



@router.get("/{id}",response_model=ResponseSchema,response_model_exclude_none=True)
async def get_person_by_id(
    person_id:int=Path(...,alias="id")
):
    result = await PersonRepository.get_by_id(person_id)
    return ResponseSchema(detail="successfully fetch person by id!",result=result)

    


@router.get("",response_model=ResponseSchema,response_model_exclude_none=True)
async def get_all_person(
          page:int = 1,
          limit:int = 10,
          columns: str = Query(None, alias="columns"),
          sort:str = Query(None, alias="sort"),
          filter:str = Query(None, alias="filter")

):
    result = await PersonRepository.get_all(page, limit, columns, sort, filter)
    return  ResponseSchema(detail="",result=result)

