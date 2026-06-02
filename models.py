from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, field_validator
from database import Base


class DBBook(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="대여가능")


class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    year: int
    status: str = "대여가능"

    @field_validator("title", "author", "publisher", "status")
    @classmethod
    def text_must_not_be_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("빈 값은 입력할 수 없습니다.")
        return v

    @field_validator("year")
    @classmethod
    def year_must_be_valid(cls, v: int) -> int:
        if v < 1000 or v > 2100:
            raise ValueError("올바른 출판연도를 입력해주세요.")
        return v


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    year: int
    status: str

    class Config:
        from_attributes = True
