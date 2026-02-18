# CRM Software – Customer & Lead Management System

A full-stack Customer Relationship Management (CRM) web application built using Flask.
This system allows businesses to manage users, customers, and sales leads with secure authentication and role-based access control.

---

## Project Overview

This CRM application provides:

* User Registration and Login
* Role-based access (Admin / Sales)
* Lead Management (Create, View, Update, Delete)
* JWT Authentication
* Professional UI with responsive design
* Deployment-ready structure

The project is structured for production deployment using Gunicorn and cloud hosting platforms like Render.

---

## Tech Stack

Backend:

* Python
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* Gunicorn (Production WSGI server)

Frontend:

* HTML5
* CSS3 (Professional UI styling)
* JavaScript (Fetch API)

Database:

* SQLite (Development)
* PostgreSQL (Production recommended)

Deployment:

* GitHub
* Render

---

## Project Structure

```
backend/
│
├── app.py
├── wsgi.py
├── models.py
├── auth.py
├── routes.py
├── config.py
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── leads.html
│
└── static/
    ├── app.js
    └── styles.css
```

---

## Features

User Management

* User registration
* Secure password hashing
* Login with JWT token authentication
* Role selection (Admin / Sales)

Lead Management

* Add new leads
* View all leads
* Update lead status
* Delete leads

Security

* JWT-based authentication
* Protected API routes
* Password hashing using Werkzeug

UI

* Modern login and signup interface
* Responsive layout
* Professional button styling
* Clean dashboard layout

---

## Installation Guide (Local Setup)

1. Clone Repository

```
git clone https://github.com/yourusername/crm-system.git
cd crm-system/backend
```

2. Create Virtual Environment

```
python -m venv venv
```

3. Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

4. Install Dependencies

```
pip install -r requirements.txt
```

5. Run Application

```
python app.py
```

6. Open Browser

```
http://127.0.0.1:5000/
```

---

## Production Deployment (Render)

1. Push project to GitHub
2. Create Web Service on Render
3. Build Command:

```
pip install -r requirements.txt
```

4. Start Command:

```
gunicorn wsgi:app
```

5. Add PostgreSQL environment variable:

```
DATABASE_URL = your_postgresql_connection_string
```

After deployment, you will receive a public live URL.

---

## Environment Variables (Production)

Inside Render dashboard:

Key:

```
DATABASE_URL
```

Value:

```
PostgreSQL connection string
```

Optional:

```
SECRET_KEY
JWT_SECRET_KEY
```

---

## Future Improvements

* Email verification
* Password reset system
* Admin panel for user management
* Analytics dashboard
* Export leads to CSV
* Activity logs
* Dark mode UI

---

## Author

Noman Sameet
B.Tech – Computer Science Engineering
Flask Full Stack Developer

---

## License

This project is for educational and demonstration purposes.

---


Tell me your next goal.
