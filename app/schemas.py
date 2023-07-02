from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_superuser: bool

    class Config:
        orm_mode = True

class ResolutionBase(BaseModel):
    text: str

class ResolutionCreate(ResolutionBase):
    pass

class Resolution(ResolutionBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class SuggestionBase(BaseModel):
    text: str
    action: str

class SuggestionCreate(SuggestionBase):
    pass

class Suggestion(SuggestionBase):
    id: int
    user_id: int
    resolution_id: int

    class Config:
        orm_mode = True