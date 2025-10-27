# 🧩 Project Management Tool

A full-stack web application built to manage software projects — including project tracking, task assignment, and team management — with role-based access control (Admin, Manager, Developer).

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js (JavaScript, Axios, React Router) |
| **Backend** | FastAPI (Python) |
| **Database** | MySQL (SQLAlchemy ORM) |
| **Authentication** | JWT (JSON Web Token) |
| **Testing & Docs** | Swagger UI, Postman |
| **Bonus (Optional)** | OpenAI / Groq API for AI-generated User Stories |

---


---

## ⚙️ How to Run the Project

### 🖥 Backend Setup (FastAPI + MySQL)

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/project-management-tool.git
   cd project-management-tool/backend
2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Create .env file

DATABASE_URL=mysql+mysqlconnector://root:password@localhost:3306/pmdb
JWT_SECRET=supersecretjwtkey
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

5. Create database in MySQL

CREATE DATABASE pmdb;

6. Run the backend server

uvicorn main:app --reload --port 8000

💻 Frontend Setup (React)

1. Navigate to frontend

cd ../frontend

2. Install dependencies

npm install

3. Run React app

npm start

4. CORS Setup (if needed)
Add this snippet in main.py before routers:

from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


## 🔗 API Endpoint Summary

### 📁 Project Module (`/api/projects`)

| Method | Endpoint | Description | Required Role | Request Body Example | Response Example |
|---------|-----------|-------------|----------------|----------------------|------------------|
| **POST** | `/api/projects/` | Create a new project | Manager / Admin | ```json { "name": "Website Revamp", "description": "Rebuild company site", "deadline": "2025-12-31T00:00:00", "manager_id": 2 } ``` | ```json { "id": 1, "name": "Website Revamp", "description": "Rebuild company site", "deadline": "2025-12-31T00:00:00", "status": "Not Started", "manager_id": 2 } ``` |
| **GET** | `/api/projects/` | Fetch all projects | Any logged-in user | — | ```json [ { "id": 1, "name": "Website Revamp", "status": "Not Started" } ] ``` |
| **GET** | `/api/projects/{id}` | Fetch a single project by ID | Any logged-in user | — | ```json { "id": 1, "name": "Website Revamp", "description": "Rebuild company site", "status": "Not Started" } ``` |
| **PUT** *(optional)* | `/api/projects/{id}` | Update project details (status, name, deadline) | Manager / Admin | ```json { "status": "In Progress" } ``` | ```json { "message": "Project updated successfully" } ``` |
| **DELETE** *(optional)* | `/api/projects/{id}` | Delete a project | Admin only | — | ```json { "message": "Project deleted successfully" } ``` |

---

### ✅ Task Module (`/api/tasks`)

| Method | Endpoint | Description | Required Role | Request Body Example | Response Example |
|---------|-----------|-------------|----------------|----------------------|------------------|
| **POST** | `/api/tasks/` | Create a new task under a project | Manager / Admin | ```json { "title": "Frontend UI", "description": "Build login form", "deadline": "2025-11-15T00:00:00", "assigned_to": 3, "project_id": 1 } ``` | ```json { "id": 1, "title": "Frontend UI", "description": "Build login form", "status": "To Do", "assigned_to": 3, "project_id": 1 } ``` |
| **GET** | `/api/tasks/` | Fetch all tasks | Any logged-in user | — | ```json [ { "id": 1, "title": "Frontend UI", "status": "To Do" } ] ``` |
| **GET** | `/api/tasks?project_id=1` | Fetch all tasks for a specific project | Any logged-in user | — | ```json [ { "id": 1, "title": "Frontend UI", "project_id": 1 } ] ``` |
| **PUT** *(optional)* | `/api/tasks/{id}` | Update task status or reassign | Manager / Developer | ```json { "status": "In Progress" } ``` | ```json { "message": "Task updated successfully" } ``` |
| **DELETE** *(optional)* | `/api/tasks/{id}` | Delete a task | Manager / Admin | — | ```json { "message": "Task deleted successfully" } ``` |

---

### 🧠 Notes

- All endpoints (except register/login) require a **JWT Bearer Token** in the header:  


📊 Dashboard Metrics (Frontend)

Total projects
Total tasks (To Do, In Progress, Done)
Overdue tasks
Project progress summary


🔐 Authentication

JWT-based authentication using Bearer token
Tokens generated on login and verified for protected routes
Roles:
   Admin — Full access
   Manager — Create/edit projects and assign tasks
   Developer — View/update assigned tasks

💡 Assumptions

Each project is managed by one Project Manager
Developers are assigned tasks; they cannot create/delete them
Only Managers/Admins can create new projects or tasks
Passwords hashed using bcrypt
JWT stored in localStorage for simplicity
Comments, attachments, and notifications are not implemented yet

🧠 Improvements Possible
Area	Suggested Improvement
Security	Add refresh tokens, password reset, and httpOnly cookies
Database	Many-to-many user–project relationship for team assignments
UI/UX	Use Material UI or TailwindCSS for design polish
Testing	Add PyTest for backend and React Testing Library for frontend
Notifications	Email or in-app alerts for deadlines
AI Integration (Bonus)	/api/ai/generate-user-stories using OpenAI/Groq API
Deployment	Dockerize backend, frontend, and MySQL
Analytics	Add charts using Recharts or Chart.js

🧾 License

This project was built for internship evaluation purposes.
You may reuse and extend it for learning or educational use.

