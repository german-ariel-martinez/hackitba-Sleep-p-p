from typing import Optional
from pydantic import BaseModel
from datetime import date, time

class CompleteUser(BaseModel):
    username: str
    password: str
    description: Optional[str]
    pictureId: Optional[int]
    birthdate: date
    email: str
    website: Optional[str]
    linkedin: Optional[str]

class User(BaseModel):
    user_id: int
    username: str
    description: Optional[str]
    pictureId: Optional[int]
    birthdate: date
    rank: int
    isVerified: bool
    email: str
    website: Optional[str]
    linkedin: Optional[str]

class Post(BaseModel):
    title: str
    text: str
    author: str
    parentPostId: Optional[int]
   

class Response(BaseModel):
    status: int
    detail: dict


class Comment(BaseModel):
    author: str
    text: str  

class Credentials(BaseModel):
    username: str
    password: str

class Company(BaseModel):
    name: str
    description: str

class AMA_post(BaseModel):
    title: str
    text: str
    author: str
    
