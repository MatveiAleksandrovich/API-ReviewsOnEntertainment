FROM python:3.8.5

WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r /code/requirements.txt
RUN pip3 install psycopg2-binary
COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
