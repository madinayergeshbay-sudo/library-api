from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library Book Rental Management System",
    description="FastAPI + SQLAlchemy + SQLite MVC 패턴 도서관 책 대여 관리 시스템",
    version="1.0.0"
)


@app.get("/", tags=["health"])
def root():
    return {
        "message": "도서관 책 대여 관리 시스템 서버가 정상 실행 중입니다.",
        "docs": "http://127.0.0.1:8000/docs"
    }


@app.post("/books/", response_model=models.BookResponse, status_code=201, tags=["books"])
def create_book(book: models.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@app.get("/books/", response_model=list[models.BookResponse], tags=["books"])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@app.get("/books/{book_id}", response_model=models.BookResponse, tags=["books"])
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="도서를 찾을 수 없습니다.")
    return book


@app.put("/books/{book_id}", response_model=models.BookResponse, tags=["books"])
def update_book(book_id: int, book: models.BookCreate, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db, book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="수정할 도서를 찾을 수 없습니다.")
    return updated_book


@app.delete("/books/{book_id}", tags=["books"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = crud.delete_book(db, book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="삭제할 도서를 찾을 수 없습니다.")
    return {"message": f"{deleted_book.title} 도서가 삭제되었습니다."}
