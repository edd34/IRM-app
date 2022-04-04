#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ ! -d ./staticfiles ]
then
    mkdir staticfiles
fi

python manage.py collectstatic --no-input
python manage.py flush --no-input
python manage.py migrate
python3 manage.py init_alerte_table

exec "$@"
