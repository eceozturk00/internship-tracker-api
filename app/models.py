from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False, default="Applied")  # Applied/Interview/Offer/Rejected
    link = Column(String(500), nullable=True)
    notes = Column(Text, nullable=True)
    applied_date = Column(String(20), nullable=True)  # keep simple (e.g., 2026-03-04)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
