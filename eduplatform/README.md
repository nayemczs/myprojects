# EduPlatform — School/College Management System

Multi-portal education platform: public website + Admin, Teacher, and Student portals.
**Stack:** React (Vite) · Django REST Framework · SQLite (default) or PostgreSQL · JWT auth.

## Run the backend
```bash
cd backend
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```
API at http://localhost:8000/api/ , Django admin at /admin/ .

## Run the frontend
```bash
cd frontend
npm install
npm run dev
```
Open http://localhost:5173 .

## Demo accounts (password: password123)
principal · admin1 · teacher_physics · student1

## Switching to PostgreSQL
Edit `backend/.env`, set `DB_ENGINE=postgres` and fill the `DB_*` values, then re-run migrate + seed.
