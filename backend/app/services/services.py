from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# -------------------- USER SCHEMAS --------------------

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    college: Optional[str] = None
    domain: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    college: Optional[str] = None
    domain: Optional[str] = None


class UserOut(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# -------------------- DOMAIN SCHEMAS --------------------

class DomainBase(BaseModel):
    name: str
    description: Optional[str] = None


class DomainOut(DomainBase):
    id: int

    class Config:
        orm_mode = True
