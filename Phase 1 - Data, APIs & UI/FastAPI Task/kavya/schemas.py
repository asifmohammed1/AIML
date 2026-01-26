from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    """Schema for creating a new employee"""
    pass

class EmployeeUpdate(BaseModel):
    """Schema for updating an existing employee (all fields optional)"""
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None

class Employee(EmployeeBase):
    """Schema for returning employee data (includes ID)"""
    id: int

    # Pydantic V2 way to allow compatibility with SQLAlchemy objects
    model_config = ConfigDict(from_attributes=True)