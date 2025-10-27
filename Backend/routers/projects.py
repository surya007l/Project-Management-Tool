# routers/projects.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ProjectCreate, ProjectOut
from crud import create_project, list_projects, get_project
from auth import get_current_user, require_role
from models import RoleEnum

router = APIRouter(prefix="/api/projects", tags=["projects"])

@router.post("/", response_model=ProjectOut)
def create(p: ProjectCreate, db: Session = Depends(get_db), current_user=Depends(require_role(RoleEnum.manager))):
    return create_project(db, p)

@router.get("/", response_model=list[ProjectOut])
def read_all(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return list_projects(db)

@router.get("/{project_id}", response_model=ProjectOut)
def read_one(project_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    pr = get_project(db, project_id)
    if not pr:
        raise HTTPException(status_code=404, detail="Project not found")
    return pr
