# School Management System (DRF)

A comprehensive Django REST Framework-based school management system designed to streamline administrative, academic, and financial operations in educational institutions.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [App Modules](#app-modules)
- [Database Models](#database-models)
- [Authentication & Permissions](#authentication--permissions)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Functionality

- **User Management**: Manage students, teachers, and admin users with role-based access control
- **Academic Management**: Handle courses, subjects, class sections, and curriculum planning
- **Attendance Tracking**: Automated attendance management for students
- **Exam Management**: Create, manage, and track exam schedules and results
- **Fee Management**: Monitor student fees, payments, and financial transactions
- **Permissions & Security**: Fine-grained permission system for different user roles

### Technical Features

- RESTful API endpoints following best practices
- Token-based authentication
- Role-based access control (RBAC)
- Comprehensive serializers for data validation
- Permission classes for endpoint security
- Database migrations for version control
- Signal-based automation
- Unit tests for critical functionality

## Project Structure

```
school_management_system_drf/
├── school_management/          # Main project settings
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL configuration
│   ├── wsgi.py                 # WSGI application
│   └── asgi.py                 # ASGI application
├── accounts/                   # User authentication & management
├── students/                   # Student information & management
├── teachers/                   # Teacher information & management
├── academics/                  # Academic & course management
├── attendance/                 # Attendance tracking
├── exams/                      # Exam management
├── fees/                       # Financial & fee management
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database
└── README.md                   # This file
```

## Technology Stack

- **Backend Framework**: Django 4.x
- **REST API**: Django REST Framework (DRF)
- **Database**: SQLite3 (Development) / PostgreSQL (Production recommended)
- **Authentication**: Django Token Authentication
- **Python Version**: 3.8+

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (venv or virtualenv)

### Steps

1. **Clone the Repository**

   ```bash
   git clone school_management_system_drf.git
   cd school_management_system_drf
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files** (if needed)
   ```bash
   python manage.py collectstatic
   ```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Settings File

Key configurations in `school_management/settings.py`:

- `INSTALLED_APPS`: Register all Django apps
- `DATABASES`: Configure database connection
- `REST_FRAMEWORK`: Configure DRF settings
- `AUTHENTICATION_CLASSES`: Set authentication method
- `PERMISSION_CLASSES`: Set default permission classes

## Running the Application

### Development Server

Start the development server:

```bash
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000/`

### Access Admin Panel

```bash
http://127.0.0.1:8000/admin/
```

Use superuser credentials created during installation.

## API Documentation

### Authentication

All API endpoints require authentication. Include the token in the request header:

```bash
Authorization: Token <your-token-here>
```

### Base URL

```
http://localhost:8000/api/
```

### Available Endpoints

Endpoints are organized by app modules:

- `/api/accounts/` - User authentication and profile management
- `/api/students/` - Student information and records
- `/api/teachers/` - Teacher information and records
- `/api/academics/` - Courses, subjects, and academic data
- `/api/attendance/` - Attendance records
- `/api/exams/` - Exam schedules and results
- `/api/fees/` - Fee management and payments

## App Modules

### 1. Accounts (`accounts/`)

Handles user authentication, registration, and user profiles.

**Key Files:**

- `models.py` - User model extensions
- `serializers.py` - User serializers
- `views.py` - Authentication views
- `permissions.py` - Custom permission classes
- `signals.py` - Signal handlers for user events

### 2. Students (`students/`)

Manages student information, enrollment, and records.

**Key Files:**

- `models.py` - Student model
- `serializers.py` - Student serializers
- `views.py` - Student API views
- `permissions.py` - Student access permissions

### 3. Teachers (`teachers/`)

Manages teacher information and assignments.

**Key Files:**

- `models.py` - Teacher model
- `serializers.py` - Teacher serializers
- `views.py` - Teacher API views

### 4. Academics (`academics/`)

Handles course, subject, and academic structure management.

**Key Files:**

- `models.py` - Course and Subject models
- `serializers.py` - Academic serializers
- `views.py` - Academic API views

### 5. Attendance (`attendance/`)

Tracks student attendance records.

**Key Files:**

- `models.py` - Attendance model
- `serializers.py` - Attendance serializers
- `views.py` - Attendance API views

### 6. Exams (`exams/`)

Manages exam schedules, results, and grading.

**Key Files:**

- `models.py` - Exam model
- `serializers.py` - Exam serializers
- `views.py` - Exam API views

### 7. Fees (`fees/`)

Manages student fees, payments, and financial records.

**Key Files:**

- `models.py` - Fee model
- `serializers.py` - Fee serializers
- `views.py` - Fee API views

## Database Models

### Key Relationships

- **User** (Django built-in) → Foundation for authentication
- **Student** → Extends User for student-specific information
- **Teacher** → Extends User for teacher-specific information
- **Course** → Academic offerings
- **Subject** → Course components
- **Attendance** → Tracks student presence
- **Exam** → Manages exam information
- **Fee** → Handles financial data

## Authentication & Permissions

### Authentication Methods

- Token Authentication (REST Framework)
- Session Authentication (Django)

### Permission Classes

Each app implements custom permission classes:

- `IsAdmin` - Only admin users
- `IsTeacher` - Only teachers
- `IsStudent` - Only students
- `IsOwner` - Only resource owner
- `ReadOnly` - View-only access

## Testing

Run tests for specific apps:

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test accounts
python manage.py test students
python manage.py test academics

# Run with verbose output
python manage.py test --verbosity=2
```

Test files are located in each app's `tests.py` file.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Write unit tests for new features

## Common Commands

```bash
# Create migrations for an app
python manage.py makemigrations <app_name>

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Shell access
python manage.py shell

# Check project for issues
python manage.py check

# Create new app
python manage.py startapp <app_name>
```

## Troubleshooting

### Migration Issues

```bash
# Reset migrations for an app (development only)
python manage.py migrate <app_name> zero
python manage.py migrate <app_name>
```

### Database Issues

```bash
# Reset entire database (development only)
rm db.sqlite3
python manage.py migrate
```

### Permission Denied Errors

- Verify user has appropriate role
- Check permission classes in views
- Ensure token is valid and included in headers

## Future Enhancements

- [ ] Email notifications for events
- [ ] SMS alerts for attendance
- [ ] Mobile app integration
- [ ] Advanced analytics dashboard
- [ ] Document management system
- [ ] Student portal
- [ ] Parent notification system
- [ ] Grade calculation engine

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Last Updated**: February 15, 2026

**Version**: 1.0.0
