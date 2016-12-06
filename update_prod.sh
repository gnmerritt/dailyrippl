#!/bin/bash
set -e
echo "Updating checkout"
git pull

echo "Updating static files"
export DJANGO_SETTINGS_MODULE=rippl.prod_settings
python rippl/manage.py collectstatic --noinput
rsync -avz static/ nathan@scorpion.local:~/rippl/static/

if [ -f rippl-gunicorn.pid ]; then
  echo "Stopping running server"
  kill `cat rippl-gunicorn.pid`
fi
bash start_prod.sh
