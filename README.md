If you're accessing it from your terminal, you'd need to install couple of things first. Please, follow the instructions mentioned below.


Accessing from the Gitpod terminal:
- pip3 install django
- pip3 install django-allauth==0.41.0
- pip install Pillow
- python3 manage.py migrate
- python3 manage.py loaddata categories
- python3 manage.py loaddata projects

Accessing as a superuser:
- python3 manage.py createsuperuser
and insert your name, email and password.

