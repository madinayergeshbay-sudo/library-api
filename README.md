# 📚 도서관 책 대여 관리 시스템

## 프로젝트 소개

FastAPI와 SQLite를 활용한 MVC 패턴 기반 도서관 도서 대여 관리 시스템입니다.

## 사용 기술

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- MVC Pattern

## 프로젝트 구조


## 주요 기능

### 도서 등록
POST /books/

### 전체 도서 조회
GET /books/

### 특정 도서 조회
GET /books/{book_id}

### 도서 수정
PUT /books/{book_id}

### 도서 삭제
DELETE /books/{book_id}

## API 테스트

Swagger UI를 통해 API를 테스트할 수 있습니다.

http://127.0.0.1:8000/docs

## MVC 구조

### Model
models.py

### Controller
main.py

### Database
database.py

### CRUD
crud.py

## 개발자

Madina

경복대학교 빅데이터과
