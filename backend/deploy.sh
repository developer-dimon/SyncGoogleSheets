#!/bin/sh
python manage.py migrate
python manage.py collectstatic
gunicorn SyncGoogleSheets.wsgi:application --bind 0.0.0.0:${DJANGO_PORT}
