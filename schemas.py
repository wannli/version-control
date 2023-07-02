from pydantic import BaseModel
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    username: str
    email: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str


# SuperUser Schemas
class SuperUserBase(BaseModel):
    username: str
    email: Optional[str] = None

class SuperUserCreate(SuperUserBase):
    password: str

class SuperUser(SuperUserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class SuperUserInDB(SuperUser):
    hashed_password: str


# Resolution Schemas
class ResolutionBase(BaseModel):
    title: str
    content: str

class ResolutionCreate(ResolutionBase):
    pass

class Resolution(ResolutionBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ResolutionInDB(Resolution):
    pass


# Suggestion Schemas
class SuggestionBase(BaseModel):
    resolution_id: int
    content: str
    type: str  # add, delete, replace

class SuggestionCreate(SuggestionBase):
    pass

class Suggestion(SuggestionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class SuggestionInDB(Suggestion):
    pass