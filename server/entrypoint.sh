#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear

if "$DEBUG"; then
  exec python3 manage.py runserver 0.0.0.0:8000
else
  exec "$@"
fi