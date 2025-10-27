# routers/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserCreate, UserOut, Token
from crud import create_user, authenticate_user
from auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/api/users", tags=["users"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        u = create_user(db, user)
        return u
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"user_id": user.id, "role": user.role.value})
    return {"access_token": token, "token_type": "bearer"}
