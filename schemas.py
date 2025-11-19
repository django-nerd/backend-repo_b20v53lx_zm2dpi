from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Contact(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    message: str = Field(..., min_length=10, max_length=5000)
    budget: Optional[str] = Field(None, description="Client budget range")

# Example additional models you might add later for a portfolio site
class Testimonial(BaseModel):
    name: str
    role: str
    quote: str

class Project(BaseModel):
    title: str
    tag: Optional[str] = None
    image_url: Optional[str] = None
    url: Optional[str] = None
