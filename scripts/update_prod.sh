#!/bin/bash
set -e
echo "Updating checkout"
git pull

echo "Installing deps"
source /home/rippl/venvs/rippl/bin/activate # TODO: make this less snowflake
pip install -r requirements.txt
# TODO: install npm so we can build frontend
# npm install
# brunch build

echo "Updating static files"
source PROD_ENV.sh
export DJANGO_SETTINGS_MODULE=rippl.prod_settings
python rippl/manage.py collectstatic --noinput
rsync -avz static/ nathan@scorpion.local:~/rippl/static/

PIDFILE="rippl/gunicorn.pid"
if [ -f "$PIDFILE" ]; then
  echo "Stopping running server"
  kill `cat "$PIDFILE"`
fi
bash start_prod.sh
