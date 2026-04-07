# Django Webpage

## 📌 Overview

This project is a **Django-based web application** that functions as a simple social media / blog platform. Users can create accounts, log in, and share posts that are displayed on a homepage feed. It mostly focused on the back-end and not the frot-end.

---

## 🚀 Features

* 🔐 User authentication (Sign up, Login, Logout)
* 📝 Create and view posts
* 🏠 Dynamic homepage feed

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** Django models (Admin)

---

## 📂 Project Structure

```
Django-Webpage/
│── webapp/              # Main Django app
│   ├── templates/       # HTML templates
│   ├── static/          # CSS and static files
│   ├── models.py        # Database models
│   ├── views.py         # Application logic
│   ├── urls.py          # App routes
│
│── myproject/           # Project configuration
│── manage.py            # Django CLI tool
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/osvat0rres/Django-Webpage.git
cd Django-Webpage
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Run migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

### 6. Open in browser

```
http://127.0.0.1:8000/
```

---

## 🧠 How It Works

* Users register and log in to the platform
* Authenticated users can create posts
* Posts are stored in the database and displayed on the homepage
* Django templates dynamically render content


---
