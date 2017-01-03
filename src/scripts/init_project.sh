#!/usr/bin/env bash

docker run \
    --name bojamo-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e POSTGRES_USER=user \
    -e POSTGRES_DB=bojamo_db \
    -p 54321:5432 \
    -d postgres:9.5

cd ..
python3 manage.py makemigrations
python3 manage.py migrate
./apply_mock.py

sudo apt-get install libpq-dev python-psycopg2
