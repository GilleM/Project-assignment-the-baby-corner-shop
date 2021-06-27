This is the project that had to be done for a certain course I applied for. I started with the project as soon as I got the notion of it, 24th of June after work (at 21h) trying to catch up with it until 27th of June 23:59h. 
I was working every day long shifts (weekends included) and I started from scratch, so the project stayed not accomplished due to lack of time.


If you're accessing it from your terminal, you'd need to install couple of things first. Please, follow the instructions mentioned below.


Accessing from the Gitpod terminal:
- pip3 install django
- pip3 install django-allauth==0.41.0
- pip install Pillow
- python3 manage.py migrate
- python3 manage.py loaddata categories
- python3 manage.py loaddata projects

In case if superuser would need to be created, please write:
- python3 manage.py createsuperuser
and insert your name, email and password.

Requirements:

- User must be able to add an item to the shopping list

- User must be able to view their whole shopping list

- User must be able to delete an individual item from the shopping list

- User must be able to delete their entire shopping list, with a single button click (without going and deleting each individual item one by one) 

- Each user must be able to login with their Google account and their shopping list must persist between their logins