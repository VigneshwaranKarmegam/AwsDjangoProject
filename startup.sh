#!/bin/bash
#python manage.py collectstatic && gunicorn --workers 2 api_crud.wsgi
python3 manage.py migrate && python3 manage.py collectstatic && gunicorn --workers 2 api_crud.wsgi