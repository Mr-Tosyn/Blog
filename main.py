from fastapi import FastAPI

app = FastAPI


@app.get('/')
def index():
    return {'data': 'blog list'}


@app.get('/blog/{id}')
def show():
    # fetch blog with id = id
    return {'data':1}


@app.get('/blog/{id}/comments')
def comments(id):
     # fetch comments of blog with id = id
    return {'data':{'1', '2'}}
