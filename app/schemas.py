from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

StatusType = Literal["Applied", "Interview", "Offer", "Rejected"]

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ApplicationCreate(BaseModel):
    company: str = Field(min_length=2)
    role: str = Field(min_length=2)
    status: StatusType = "Applied"
    link: Optional[str] = None
    notes: Optional[str] = None
    applied_date: Optional[str] = None  # YYYY-MM-DD

class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[StatusType] = None
    link: Optional[str] = None
    notes: Optional[str] = None
    applied_date: Optional[str] = None

class ApplicationOut(BaseModel):
    id: int
    company: str
    role: str
    status: str
    link: Optional[str]
    notes: Optional[str]
    applied_date: Optional[str]

    class Config:
        from_attributes = True
