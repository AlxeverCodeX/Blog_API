from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return 'heyy'

class Blog(BaseModel): 
    title:str
    body:str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request_body: Blog):
    return {'data': 'Blog is created'} 