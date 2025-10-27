# routers/tasks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import TaskCreate, TaskOut
from crud import create_task, list_tasks
from auth import get_current_user, require_role
from models import RoleEnum

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

@router.post("/", response_model=TaskOut)
def create(t: TaskCreate, db: Session = Depends(get_db), current_user=Depends(require_role(RoleEnum.manager))):
    return create_task(db, t)

@router.get("/", response_model=list[TaskOut])
def read_all(project_id: int = None, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return list_tasks(db, project_id=project_id)
