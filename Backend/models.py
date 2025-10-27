# models.py
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
import enum
import datetime

class RoleEnum(str, enum.Enum):
    admin = "admin"
    manager = "manager"
    developer = "developer"

class ProjectStatus(str, enum.Enum):
    not_started = "Not Started"
    in_progress = "In Progress"
    completed = "Completed"

class TaskStatus(str, enum.Enum):
    todo = "To Do"
    in_progress = "In Progress"
    done = "Done"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(200))
    role = Column(Enum(RoleEnum), default=RoleEnum.developer)

    projects_managed = relationship("Project", back_populates="manager")
    assigned_tasks = relationship("Task", back_populates="assignee")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), index=True)
    description = Column(Text)
    deadline = Column(DateTime, nullable=True)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.not_started)
    manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    manager = relationship("User", back_populates="projects_managed")
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150))
    description = Column(Text)
    status = Column(Enum(TaskStatus), default=TaskStatus.todo)
    deadline = Column(DateTime, nullable=True)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"))

    assignee = relationship("User", back_populates="assigned_tasks")
    project = relationship("Project", back_populates="tasks")
