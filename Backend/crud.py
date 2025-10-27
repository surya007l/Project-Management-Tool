# crud.py
from sqlalchemy.orm import Session
from models import User, Project, Task
from auth import get_password_hash, verify_password
from schemas import UserCreate, ProjectCreate, TaskCreate
from datetime import datetime

# Users
def create_user(db: Session, user: UserCreate):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise ValueError("Email already registered")
    hashed = get_password_hash(user.password)
    u = User(name=user.name, email=user.email, password=hashed, role=user.role)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

# Projects
def create_project(db: Session, project: ProjectCreate):
    p = Project(
        name=project.name,
        description=project.description,
        deadline=project.deadline,
        manager_id=project.manager_id,
        status="Not Started"
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def list_projects(db: Session, skip=0, limit=100):
    return db.query(Project).offset(skip).limit(limit).all()

# Tasks
def create_task(db: Session, task: TaskCreate):
    t = Task(
        title=task.title,
        description=task.description,
        deadline=task.deadline,
        assigned_to=task.assigned_to,
        project_id=task.project_id,
        status="To Do"
    )
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

def list_tasks(db: Session, project_id: int = None):
    q = db.query(Task)
    if project_id:
        q = q.filter(Task.project_id == project_id)
    return q.all()
