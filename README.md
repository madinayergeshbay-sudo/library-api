# 📚 Library Management System

## 👩‍🎓 Student Information

- Name: Madina Yergeshbay
- University: Kyungbok University
- Department: Big Data
- Course: Application Development
- Project: Library Book Rental Management System

---

## 📖 Project Overview

This project is a Library Book Rental Management System developed using FastAPI, SQLAlchemy and SQLite.

The system allows users to:

- Add new books
- View all books
- Search books by ID
- Update book information
- Delete books

---

## 🛠 Technology Stack

| Technology | Description |
|------------|-------------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| SQLAlchemy | ORM |
| SQLite | Database |
| Pydantic | Data Validation |

---

## 📂 Project Structure

```text
library_api_project/
│
├── main.py
├── models.py
├── crud.py
├── database.py
├── requirements.txt
├── README.md
└── library.db
```

## 🚀 API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | / | Server Status |
| POST | /books/ | Create Book |
| GET | /books/ | Get All Books |
| GET | /books/{book_id} | Get Book |
| PUT | /books/{book_id} | Update Book |
| DELETE | /books/{book_id} | Delete Book |

---

## 💾 Database

SQLite database is used for storing book information.

Book information includes:

- Title
- Author
- Publisher
- Year
- Status

---

## 📷 Swagger UI

After running the server:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## ✅ Project Features

✔ FastAPI REST API

✔ MVC Pattern

✔ CRUD Operations

✔ SQLite Database

✔ Swagger Documentation

✔ GitHub Version Control

---

## 👏 Thank You
Kyungbok University - Big Data Department
