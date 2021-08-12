from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette import status
from blog import schemas, database, oauth2
from typing import List
from blog.repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(
    db: Session = Depends(get_db), 
    get_current_user: schemas.User = Depends(oauth2.get_current_user)
):

    return blog.get_all(db=db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Blog, 
    db: Session = Depends(get_db), 
    get_current_user: schemas.User = Depends(oauth2.get_current_user)
):

    return blog.create(request=request, db=db)

@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(
    id, 
    db: Session = Depends(get_db), 
    get_current_user: schemas.User = Depends(oauth2.get_current_user)
):

    return blog.destroy(id=id, db=db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(
    id, 
    request: schemas.Blog, 
    db: Session = Depends(get_db), 
    get_current_user: schemas.User = Depends(oauth2.get_current_user)
):

    return blog.update(id=id, request=request, db=db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(
    id, 
    db: Session = Depends(get_db), 
    get_current_user: schemas.User = Depends(oauth2.get_current_user)
):

    return blog.show(id=id, db=db)
