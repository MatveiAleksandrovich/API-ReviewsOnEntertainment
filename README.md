# api_yamdb
### Описание
Это проект API для публикации отзывов на различные фильмы, книги, газеты и т.д.
Категории, жанры можно добавлять также самостоятельно.
### Технологии
Python 3.7
Django 2.2.19

### Запуск проекта
```
docker-compose up -d --build 
``` 

### Создание суперпользователя

 ```
docker-compose exec web python manage.py createsuperuser
```

### Заполнение базы начальными данными

```
docker-compose exec web python manage.py migrate --noinput
```

### Авторы
Матвей Александрович, Евгений Парыгин, Дмитрий Бабешко 

=======
![yamdb_workflow](https://github.com/MatveiAleksandrovich/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
>>>>>>> 743a51e0bc5630ee2e1b9872b9b2a453a79f619e

http://130.193.53.174/admin/login/?next=/admin/
