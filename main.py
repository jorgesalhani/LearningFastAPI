from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data': 'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished'}

@app.get("/blog/{id}")
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {id}}