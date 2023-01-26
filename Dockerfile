FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1 

WORKDIR /app_cnab_parser

COPY . . 

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations