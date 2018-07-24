### REST API

This application is a simple CRUD API with Django rest


### Technologies used
The functionality of this web app depends on the following technologies.

- Django
- Django REST Framework
- Django rest JWT
- Postgres


### Installation
- Download or clone the app on your local machine
- Move into local directory cd into the directory
- Activate virtaul environment
- Run `pip install -r requirements.txt`
- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Run `python manage.py createsuperuser` and follow the prompt to create an account
- Run `python manage.py runserver`
- Visit `http://localhost:8000/api/v1/token-auth/ ` and log in with email and password you used in creation.
- Grab the token and pass it as Authorization Header in the format `JWT <token>`
- The POST method of `localhost:8080/api/v1/list/` will post user to the app `email` and `name` 
- The GET method of `localhost:8000/api/v1/list/ ` will retrieve users in the app
- The GET method of `localhost:8000/api/v1/list/:id` will retrieve a particular user with the id
- Run `python manage.py test` to run test

### Author
This is done by Sasiliyu Adetunji

### License & Copyright
MIT © Sasiliyu Adetunji Licensed under the MIT License.