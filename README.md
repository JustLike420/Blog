# Django project - Blog


### Creating venv
```
python -m venv venv
```
```
.\venv\Scripts\activat
```
____
### Installing Django
```
pip install Django
```
____
### Creating project
```
django-admin startproject siteblog
```
____
### Creating new app - SiteBlog
```
python manage.py createapp siteblog
```
____
### Static files
```
python manage.py collectstatic
```
_____
### Creating DB
```
python manage.py makemigrations
```
```
python manage.py migrate
```
