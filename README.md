# Support Intelligence API

A Python-based support-ticket management API built with FastAPI, MySQL,
SQLAlchemy, Docker, PyTest, Flake8, and Git.

## Problem Statement

Support teams need a centralized system to create, track, update, and
analyze technical issues. This project provides REST APIs for structured
ticket management and support workflow automation.

## Features

- Create support tickets
- View all tickets
- Search tickets by ID
- Update ticket status
- Store tickets in MySQL
- Priority classification
- Health-check endpoint
- External API integration
- Automated API testing
- Docker-based deployment
- Flake8 code-quality checks

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Docker
- PyTest
- Flake8
- Git

## How to Run

### Start the database

```bash
docker compose up -d mysql
```

### Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the API

```bash
python -m uvicorn main:app --reload
```

## API Documentation

Open:

http://127.0.0.1:8000/docs

## Run Tests

```bash
pytest -v
```

## Run Code Quality Checks

```bash
flake8 .
```

## Project Structure

```text
main.py             API routes and application setup
database.py         Database connection
models.py           MySQL database models
ticket_service.py   Business logic
tests/              Automated tests
Dockerfile          API container configuration
docker-compose.yml  MySQL and Docker configuration
```

## Future Improvements

- User authentication
- Role-based access
- Dashboard for ticket metrics
- AI-powered document search
- LangChain and ChromaDB integration
- Deployment to a cloud platform
