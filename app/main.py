from fastapi import FastAPI
from .db import Base, engine
from .routes.applications import router as applications_router

app = FastAPI(
    title="Internship Tracker API",
    description="Track internship applications with a clean REST API.",
    version="1.0.0"
)

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(applications_router)

@app.get("/")
def root():
    return {"message": "Internship Tracker API is running ✅"}
