#!/bin/bash

python ./ecommerce/manage.py migrate
python ./ecommerce/manage.py collectstatic --clear --noinput
gunicorn --bind 0.0.0.0:8000 --chdir ./ecommerce ecommerce.wsgi --workers 3
