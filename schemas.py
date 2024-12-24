# schemas.py

from pydantic import BaseModel, conint

class BookBase(BaseModel):
    title: str
    author: str
    available_copies: conint(ge=0)  # Ensure available copies is non-negative

class BookCreate(BookBase):
    pass

class Book(BookBase):
    book_id: int

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class MemberBase(BaseModel):
    name: str

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    member_id: int

    class Config:
        orm_mode = True

class LoanBase(BaseModel):
    book_id: int
    member_id: int

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    loan_id: int

    class Config:
        orm_mode = True
