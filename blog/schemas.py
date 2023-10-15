from pydantic import BaseModel
from datetime import datetime
class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(BaseModel):
    title: str
    body: str
    timestamp: datetime = datetime.now()
    class config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str
    