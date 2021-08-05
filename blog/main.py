from fastapi import FastAPI
from blog.schemas import Blog
from blog import models
from blog.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/blog')
def create(request: Blog):
    return request