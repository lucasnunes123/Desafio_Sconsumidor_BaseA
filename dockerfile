FROM python:3.9
LABEL author='Lucas Vinícius Nunes do Nascimento'

USER root

COPY . /base_a_app

RUN pip install django && pip install djangorestframework

VOLUME /base_a_app
WORKDIR /base_a_app

EXPOSE 8000

CMD  python ./manage.py makemigrations && python ./manage.py migrate\
    && python ./manage.py runserver

