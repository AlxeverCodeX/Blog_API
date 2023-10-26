from pydantic import BaseModel
from datetime import datetime
from typing import List


class BlogBase(BaseModel):
    #id : int
    title: str
    body: str
    

class Blog(BlogBase):
    class config():
        orm_mode = True



class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] = []
    class config():
        orm_mode = True


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser
    timestamp: datetime = datetime.now()

    class config():
        orm_mode = True


class Login(BaseModel):
    username:str
    password:str




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None