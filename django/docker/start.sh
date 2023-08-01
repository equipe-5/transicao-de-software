#!/usr/bin/env bash

set -e

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -c "\q" 1>/dev/null 2>&1; do
    echo "Postgres is unavailable, waiting..."
    sleep 1
done

echo "Creating migrations..."
python3 /usr/src/root/django/manage.py makemigrations --noinput
echo "Finished creating migrations"

echo "Migrating models..."
python3 manage.py migrate --noinput
echo "Finished migrating models"

echo "Loading fixtures..."
# python3 manage.py loaddata */fixtures/default/*.json
# if [ "$MODE" = "production" ]; then
#     python3 manage.py loaddata */fixtures/production/*.json
# elif [ "$MODE" = "staging" ]; then
#     python3 manage.py loaddata */fixtures/staging/*.json
# elif [ "$MODE" = "development" ]; then
    python3 manage.py loaddata */fixtures/development/*.json
# fi
echo "Finished loading fixtures"

if [ "$MODE" = "development" ]; then
    echo "Starting Transition as `whoami`"
    python3 manage.py runserver 0.0.0.0:80
else
    echo "Starting Transition as `whoami`" &
    exec gunicorn main.wsgi:application \
        --name transition \
        --bind 0.0.0.0:80 \
        --workers $NUM_GUNICORN_WORKERS \
        --timeout 300 \
        --log-level=info \
        --log-file=$LOGS_ROOT/gunicorn_info.log \
        --access-logfile=$LOGS_ROOT/gunicorn_access.log
fi
