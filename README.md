# Task Management API

A modular Task Management REST API built using FastAPI, PostgreSQL, SQLAlchemy, and Pydantic.

## Features

- User Management
- Task Management
- Email Validation
- Duplicate Email Validation
- Task Status Validation
- PostgreSQL Database
- SQLAlchemy ORM
- RESTful API Endpoints
- Automated API Testing using Pytest
- Modular Project Structure

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- Uvicorn
- Git & GitHub

## Project Structure

```text
task-management-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   └── task_service.py
│   │
│   └── utils/
│       └── validators.py
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md