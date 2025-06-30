# 🏥 Healthcare Backend - Django + DRF + PostgreSQL

## Tech Stack
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication

## Setup Instructions

1. Set up `.env` with:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
2. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Start server:
   ```
   python manage.py runserver
   ```

## Auth Endpoints
- POST `/api/auth/register/`
- POST `/api/auth/login/`
- POST `/api/auth/token/refresh/`

## Patients
- CRUD: `/api/patients/`

## Doctors
- CRUD: `/api/doctors/`

## 🔁 Mapping
- `/api/mappings/`

