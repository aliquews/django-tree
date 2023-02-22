FROM python:3.10


WORKDIR /django-project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /django-project/requirements.txt
COPY ./website /django-project/website/

RUN pip install --no-cache --upgrade -r requirements.txt
