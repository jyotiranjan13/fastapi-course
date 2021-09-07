from pydantic import BaseModel
from typing import Optional,Emailstr

class UserCreate(BaseModel):
    username:str
    email:Emailstr
    hashed_password:str
    