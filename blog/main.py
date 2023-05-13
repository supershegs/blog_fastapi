from fastapi import FastAPI
from pydantic import BaseModel
from . import schemas

app = FastAPI()



@app.post('/blog')
def create(blog: schemas.Blog):
    #return {blog.title: "title", blog.body: "body"}
    return blog