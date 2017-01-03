#!/usr/bin/env bash

docker rm -f bojamo-postgres
docker run \
    --name bojamo-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e POSTGRES_USER=user \
    -e POSTGRES_DB=bojamo_db \
    -p 54321:5432 \
    -d postgres:9.5

#cd ..
sleep 10
python3 manage.py makemigrations
python3 manage.py migrate
./apply_mock.py
