# Internship Tracker API (FastAPI)

A backend project to track internship applications using a REST API.

## Features
- CRUD for internship applications (company, role, status, notes, links)
- SQLite database with SQLAlchemy
- Auto-generated Swagger docs

## Tech Stack
FastAPI, SQLite, SQLAlchemy, Pydantic, Uvicorn

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
