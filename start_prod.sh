#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HOST_IP=`ifconfig eth0 | awk '/t addr:/{gsub(/.*:/,"",$2);print$2}'`
CPUS=`grep -c ^processor /proc/cpuinfo`
JOBS=$(($CPUS + 1))
cd $DIR || exit
source PROD_ENV.sh
source /home/rippl/venvs/rippl/bin/activate # TODO: make this less snowflake
cd rippl || exit
gunicorn --env DJANGO_SETTINGS_MODULE=rippl.prod_settings \
    -b ${HOST_IP}:9000 \
    -w $JOBS \
    rippl.wsgi
