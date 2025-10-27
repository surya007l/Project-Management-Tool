# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from models import RoleEnum, ProjectStatus, TaskStatus

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: RoleEnum
    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    manager_id: Optional[int] = None

class ProjectOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    deadline: Optional[datetime]
    status: ProjectStatus
    manager_id: Optional[int]
    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    assigned_to: Optional[int] = None
    project_id: int

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    deadline: Optional[datetime]
    assigned_to: Optional[int]
    project_id: int
    class Config:
        orm_mode = True
