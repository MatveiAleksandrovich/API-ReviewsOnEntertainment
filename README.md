# Entertainment RESTful API
### Description
API project for publishing reviews of various films, books, newspapers, etc. You can also add categories, genres yourself.
I studied the advanced features of the django-rest-framework, and also worked with Docker, flake8, telegram API and set up a workflow for automated tests, pushing to DockerHub, deploying to the server and sending a telegram message about the workflow result.
### Technology
Python 3.7
Django 2.2.19
Docker
GitHub Actions
Telegram API
Cloud services

### Starting project
```
docker-compose up -d --build 
``` 

### Creating superuser

 ```
docker-compose exec web python manage.py createsuperuser
```

### Filling the database with initial data

```
docker-compose exec web python manage.py migrate --noinput
```

### Authors
Matvei Aleksandrovich, [Evgenii Parygin](https://github.com/Parygin "Named link title"), [Dmitry Babeshko](https://github.com/EnterLife "Named link title") 

=======
![yamdb_workflow](https://github.com/MatveiAleksandrovich/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
>>>>>>> 743a51e0bc5630ee2e1b9872b9b2a453a79f619e

