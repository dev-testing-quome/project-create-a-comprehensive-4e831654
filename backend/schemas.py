from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "user"

class User(BaseModel):
    id: int
    username: str
    role: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CaseCreate(BaseModel):
    title: str
    description: str
    client_name: str

class Case(BaseModel):
    id: int
    title: str
    description: str
    client_name: str
    created_at: datetime
    updated_at: datetime
    user_id: int # Add user_id

    class Config:
        orm_mode = True

class DocumentCreate(BaseModel):
    filename: str
    filepath: str
    case_id: int

class Document(BaseModel):
    id: int
    filename: str
    filepath: str
    case_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
