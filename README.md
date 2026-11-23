# 🎬 Book My Show – Movie Management System

A web-based Movie Management System developed using **Python and Django**. This application allows users to add movie details, validate movie information through Django ModelForms, and view the available movies stored in the database.

## 🚀 Features

- **Home Page:** Simple welcome page with navigation options.
- **Add New Movie:** Add movie details using Django ModelForm.
- **Form Validation:** Validates submitted movie information before saving it.
- **Movie Listing:** Displays all available movies in a structured HTML table.
- **Rating Selection:** Provides movie rating options using radio buttons.
- **Database Integration:** Stores movie information using Django ORM.
- **Django Admin Panel:** Manage movie records through the Django administration interface.
- **Static Files:** Uses CSS for styling web pages.
- **CSRF Protection:** Uses Django's built-in CSRF token for secure form submissions.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Django | Web Framework |
| SQLite | Database (Django default) |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Django ORM | Database Operations |
| Django ModelForms | Form Handling and Validation |
| Django Admin | Database Administration |

## 📂 Project Structure

```text
Book-My-Show/
│
├── manage.py
│
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── testApp/
│   ├── migrations/
│   ├── templates/
│   │   └── testApp/
│   │       ├── index.html
│   │       ├── addMovie.html
│   │       └── listMovie.html
│   │
│   ├── static/
│   │   └── css/
│   │       ├── indexStyle.css
│   │       ├── add.css
│   │       └── list.css
│   │
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── db.sqlite3
└── requirements.txt
```

*Note: Replace `project_name` with your actual Django project package name. The structure above represents the expected layout based on the shared code.*

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the Project Directory

```bash
cd Book-My-Show
```

### 3. Create a Virtual Environment

```bash
python -m venv django_env
```

### 4. Activate Virtual Environment

**Windows:**

```bash
django_env\Scripts\activate
```

**Linux / macOS:**

```bash
source django_env/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, install Django:

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/testApp/
```

## 🎥 Application Modules

### 1. Home Page

- Displays a welcome message.
- Provides navigation to the Add Movie and Available Movies sections.

### 2. Add Movie

Users can enter the following movie details:

- Movie Name
- Genre
- Director
- Actor
- Actress
- Release Date
- Language
- Movie Rating

Movie information is validated using Django ModelForms and saved to the database after successful validation.

### 3. Available Movies

- Retrieves movie records using Django ORM.
- Displays movie information in an HTML table.
- Displays an appropriate message when no movie records are available.

### 4. Django Admin Panel

The application also integrates Django Admin to manage movie records.

To access the admin panel:

```text
http://127.0.0.1:8000/admin/
```

Create an administrator account using:

```bash
python manage.py createsuperuser
```

## 🗄️ Database Model

The application uses a `Movie` model with the following fields:

| Field Name | Description |
|---|---|
| name | Movie Name |
| genre | Movie Genre |
| director | Director Name |
| actor | Actor Name |
| actress | Actress Name |
| rdate | Release Date |
| language | Movie Language |
| rating | Movie Rating |

## 🧠 Django Concepts Implemented

This project demonstrates practical implementation of:

- Django MVT (Model-View-Template) Architecture.
- URL Routing using `urls.py`.
- Function-Based Views (FBVs).
- Django Models and ORM.
- Django ModelForms.
- Form Validation using `is_valid()`.
- Saving ModelForm data using `save()`.
- GET and POST HTTP Methods.
- Django Template Language (DTL).
- Template Variables and Conditional Statements.
- Template Iteration using For Loops.
- Static File Management.
- CSRF Token Protection.
- Django Admin Customization.

## 🔮 Future Enhancements

- Implement movie search and filtering.
- Add movie update and delete functionality.
- Improve UI with responsive design.
- Add user authentication and authorization.
- Implement actual movie ticket booking functionality.

## 👨‍💻 Author

**Mangesh Natkar**

Python | Django | Java | SQL

---

⭐ If you find this project useful, feel free to star the repository!
