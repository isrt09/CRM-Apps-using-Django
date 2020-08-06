### CRM-Apps-using-Django

	- Django Customer Management Platform

# Django 3.x Cheat Sheet in a Nutshell

### Creating a virtual environment

```
python -m venv ./venv
```

### Activate the virtualenv

# Windows
venv\Scripts\activate.bat - May need to add full path (c:\users\....venv\Scripts\activate.bat)
```

### Escape from venv

```
deactivate
```

### Check packages installed in that venv

```
pip freeze
```

### Install Django

```
pip install django
```

### Create your project

```
django-admin startproject PROJECTNAME
```

### Run Server (http://127.0.0.1:8000) CTRL+C to stop

```
python manage.py runserver
```

### Create an app
```
python manage.py start app APPNAME
```

### Create migrations
```
python manage.py makemigrations
```

### Run migration
```
python manage.py migrate
```

### Create User for Admin Panel
```
python manage.py createsuperuser
```

### Collect Static Files
```
python manage.py collectstatic
```