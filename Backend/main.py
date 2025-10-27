# main.py
from fastapi import FastAPI
from database import engine, Base
from routers import users, projects, tasks
from dotenv import load_dotenv
import models

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project Management Tool")

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Project Management Tool API"}
