# catalog-service/start.sh

#!/bin/bash


python ./catalog/manage.py migrate
python ./catalog/manage.py collectstatic --clear --noinput
gunicorn --bind 0.0.0.0:8000 --chdir ./catalog catalog.wsgi --workers 3
