from sqlalchemy.orm import Session
from models import DBBook, BookCreate


def create_book(db: Session, book: BookCreate):
    db_book = DBBook(
        title=book.title,
        author=book.author,
        publisher=book.publisher,
        year=book.year,
        status=book.status
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session):
    return db.query(DBBook).order_by(DBBook.id).all()


def get_book(db: Session, book_id: int):
    return db.query(DBBook).filter(DBBook.id == book_id).first()


def update_book(db: Session, book_id: int, book: BookCreate):
    db_book = get_book(db, book_id)
    if db_book is None:
        return None

    db_book.title = book.title
    db_book.author = book.author
    db_book.publisher = book.publisher
    db_book.year = book.year
    db_book.status = book.status

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book is None:
        return None

    db.delete(db_book)
    db.commit()
    return db_book
