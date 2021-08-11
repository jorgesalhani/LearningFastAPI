from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from .. import schemas, database
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request=request, db=db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id=id, db=db)