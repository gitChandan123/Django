# Django Installation Guide

This guide will help you install Django, a high-level Python web framework, on your local machine.

## Prerequisites

Ensure the following prerequisites are met before installing Django:

1. **Python Installed**:
   - Django requires Python 3.8 or higher. Download it from [python.org](https://www.python.org/).

2. **Pip Installed**:
   - Pip is a package manager for Python. It is included with Python installations from version 3.4 and above.

3. **Virtual Environment (Optional, Recommended)**:
   - Using a virtual environment isolates your Django project dependencies.

---

## Installation Steps

### Step 1: Verify Python and Pip Installation

Run the following commands in your terminal to check the installation:

```bash
python --version
pip --version
```

Ensure both commands return valid versions.

---

### Step 2: Create a Virtual Environment (Optional)

Creating a virtual environment is recommended to avoid dependency conflicts.

1. Create the environment:
   ```bash
   python -m venv myenv
   ```

2. Activate the environment:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source myenv/bin/activate
     ```

---

### Step 3: Install Django

1. Install Django using pip:
   ```bash
   pip install django
   ```

2. Verify the installation:
   ```bash
   python -m django --version
   ```

---

### Step 4: Create a Django Project

1. Create a new Django project:
   ```bash
   django-admin startproject myproject
   ```

2. Navigate to the project directory:
   ```bash
   cd myproject
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

---

## Additional Resources


- [Django Documentation](https://docs.djangoproject.com/)
- [Python Installation Guide](https://www.python.org/downloads/)
---
Congratulations! You have successfully installed Django and set up your first project.
