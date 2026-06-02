# 도서관 책 대여 관리 시스템

FastAPI + SQLAlchemy + SQLite를 사용한 MVC 패턴 도서관 책 대여 관리 시스템입니다.

## 프로젝트 구조

```text
library_api_project/
├── database.py
├── models.py
├── crud.py
├── main.py
├── requirements.txt
└── README.md
```

## MVC 역할 분리

| 파일 | 역할 |
|---|---|
| database.py | DB 연결 및 세션 관리 |
| models.py | DB 테이블 구조와 Pydantic 데이터 검증 |
| crud.py | Create, Read, Update, Delete 로직 |
| main.py | FastAPI 앱 실행 및 API 엔드포인트 |

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
uvicorn main:app --reload
```

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

## API 엔드포인트

| Method | URL | 설명 |
|---|---|---|
| GET | / | 서버 상태 확인 |
| POST | /books/ | 도서 등록 |
| GET | /books/ | 전체 도서 조회 |
| GET | /books/{book_id} | 특정 도서 조회 |
| PUT | /books/{book_id} | 도서 정보 수정 |
| DELETE | /books/{book_id} | 도서 삭제 |

## POST 테스트 예시

```json
{
  "title": "데이터 분석 입문",
  "author": "김민수",
  "publisher": "경복출판사",
  "year": 2024,
  "status": "대여가능"
}
```

## 설명

이 프로젝트는 도서관 책 대여 관리를 위한 FastAPI 백엔드 API입니다.
SQLAlchemy로 SQLite 데이터베이스와 연결하고, Pydantic으로 입력 데이터를 검증합니다.
