from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from blog import models, schemas
from ..hashing import Hash
from starlette import status



def create_user(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name, 
        email=request.email, 
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {id} is not available'
        )
    return user