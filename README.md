# Assignment Agency

A Django-based academic assistance platform designed to help students request academic services, explore available services, view sample work, and submit project or assignment requirements.

## 🚀 Project Overview

**Assignment Agency** is a web application built with Django that provides an organized platform for academic assistance services.

The website allows visitors to:

* Explore academic services
* View sample work
* Read client reviews
* Submit a custom quote request
* Contact the agency
* Access uploaded sample documents

The project also includes a Django Admin panel for managing website content.

## ✨ Features

### Public Website

* 🏠 Home page
* 📚 Services page
* 📄 Samples page
* ⭐ Reviews page
* 💰 Custom quote request
* 📞 Contact page
* 📱 Responsive design
* 🎨 Modern and user-friendly interface

### Admin Panel

The Django Admin panel allows the administrator to manage:

* Sample documents
* Reviews
* Quote requests
* Website content

### Sample Documents

Administrators can upload sample academic documents through the Django Admin panel. Uploaded samples are automatically displayed on the website.

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **Bootstrap**
* **SQLite** (development)
* **WhiteNoise** (static files)
* **Gunicorn** (production server)

## 📁 Project Structure

```text
Assignment_Agency/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── samples/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/imran-codes-design/Assignment_Agency.git
```

### 2. Open the project directory

```bash
cd Assignment_Agency
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\env\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create an admin account

```bash
python manage.py createsuperuser
```

### 8. Collect static files

```bash
python manage.py collectstatic --noinput
```

### 9. Start the development server

```bash
python manage.py runserver
```

The website will be available at:

```text
http://127.0.0.1:8000/
```

The admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

## 🔐 Environment Variables

For production, sensitive configuration should be stored as environment variables rather than directly in the source code.

The project supports:

```text
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
```

Example:

```text
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-domain.com
DJANGO_SECRET_KEY=your-secure-secret-key
```

**Never commit production secret keys to GitHub.**

## 🗄️ Database

SQLite is currently used for local development.

For production deployment, a persistent production database such as PostgreSQL should be configured.

## 📂 Media Files

Uploaded sample documents are stored under:

```text
media/samples/
```

For production deployment, persistent cloud storage should be considered for uploaded media files.

## 🚀 Deployment

The project is prepared for deployment using:

* GitHub
* Gunicorn
* WhiteNoise
* Environment variables

Production deployment configuration may vary depending on the hosting platform.

## 🎯 Future Improvements

Planned improvements may include:

* PostgreSQL production database
* Cloud media storage
* Client account system
* Online order tracking
* Payment integration
* Email notifications
* Custom domain
* Improved SEO
* Advanced admin dashboard
* WhatsApp integration

## 👨‍💻 Author

**Muhammad Imran**

Computer Science Undergraduate

## 📄 License

This project is currently intended for educational and project-development purposes.
