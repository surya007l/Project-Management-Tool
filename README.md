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
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate

3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Create .env file
   ```bash
   DATABASE_URL=mysql+mysqlconnector://root:password@localhost:3306/pmdb
   JWT_SECRET=supersecretjwtkey
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=1440

5. Create database in MySQL
   ```bash
   CREATE DATABASE pmdb;

6. Run the backend server
   ```bash
   uvicorn main:app --reload --port 8000

💻 Frontend Setup (React)

1. Navigate to frontend
   ```bash
   cd ../frontend

2. Install dependencies
   ```bash
   npm install

3. Run React app
   ```bash
   npm start

4. CORS Setup (if needed)
   Add this snippet in main.py before routers:
   ```bash
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


---

## 🔐 Authentication

The application uses **JWT (JSON Web Token)** based authentication for secure access control.

### 🔑 How It Works
1. **Login** generates a JWT token using the `/api/users/login` endpoint.
2. The frontend stores the token in **localStorage** for subsequent requests.
3. All protected endpoints require this token to be passed in the header:


### 👥 User Roles
| Role | Permissions |
|------|--------------|
| **Admin** | Full access to manage users, projects, and tasks |
| **Manager** | Can create/edit projects and assign tasks |
| **Developer** | Can view and update their assigned tasks |

### 🧱 Token Details
- **Algorithm:** HS256  
- **Expiration:** 24 hours (configurable in `.env`)  
- **Security:** Token secret is stored in environment variables (`JWT_SECRET`)

---

## 📊 Dashboard Metrics (Frontend)

The **Dashboard** page gives an overview of project and task progress using real-time API data.

### Metrics Displayed
| Metric | Description |
|---------|-------------|
| **Total Projects** | Displays count of all active projects |
| **Total Tasks** | Displays total number of tasks across all projects |
| **Task Status Count** | Breakdown of tasks in each state — `To Do`, `In Progress`, and `Done` |
| **Overdue Tasks** | Highlights tasks whose deadlines have passed |
| **Progress Summary** | Gives an overview of completed vs. pending tasks per project |

### 🧭 Dashboard Flow
1. User logs in → redirected to `/dashboard`
2. Dashboard fetches data from:
- `/api/projects` → project count
- `/api/tasks` → task list and statuses
3. Metrics and charts (optional) are rendered dynamically using React

---

## 💡 Assumptions

- Each project is **managed by one Project Manager**.
- Only **Managers or Admins** can create or edit projects and tasks.
- **Developers** can view and update their own tasks only.
- Passwords are **securely hashed** using `bcrypt` before storage.
- **JWT token** is stored in localStorage for session management.
- Project and Task comments, notifications, and attachments are **not implemented** in this version.
- The AI-powered user story generator endpoint (`/api/ai/generate-user-stories`) is **optional** for bonus marks.

---

## 🧠 Improvements Possible

| Area | Suggested Improvement |
|------|------------------------|
| **Authentication & Security** | Implement refresh tokens, password reset, and httpOnly cookie-based tokens |
| **Database Design** | Add many-to-many relationships between Users and Projects for multi-member teams |
| **UI/UX** | Integrate Material UI or TailwindCSS for a polished design |
| **Analytics** | Add charts for task distribution and completion trends using Recharts or Chart.js |
| **Notifications** | Implement real-time notifications for new task assignments or approaching deadlines |
| **AI Integration (Bonus)** | Use OpenAI or Groq API to auto-generate user stories and tasks from project descriptions |
| **Testing** | Add unit and integration tests using PyTest (backend) and React Testing Library (frontend) |
| **Deployment** | Use Docker Compose to containerize MySQL, FastAPI, and React for production deployment |
| **Performance** | Add caching (Redis) for frequently accessed endpoints like project/task lists |
| **Role Management** | Introduce dynamic role creation and fine-grained access control |

---

✅ *These improvements can be added incrementally to evolve this project into a production-grade project management platform.*


🧾 License

This project was built for internship evaluation purposes.
You may reuse and extend it for learning or educational use.

