from typing import List, Union

from pydantic import BaseModel


class LibrarianBase(BaseModel):
    firstname: str
    lastname: str
    description: Union[str, None] = None


class ItemCreate(LibrarianBase):
    pass


class Email(BaseModel):
    pass


class Item(LibrarianBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
