#!/bin/sh
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
