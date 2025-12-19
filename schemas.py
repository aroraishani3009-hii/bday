from pydantic import BaseModel, EmailStr

class MemoryOut(BaseModel):
    id: int
    title: str
    text: str
    image: str | None
    class Config: from_attributes = True

class ContactIn(BaseModel):
    name: str
    email: EmailStr
    message: str
