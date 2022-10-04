#!/bin/sh

cd ..
docker build -t hoa_airflow .
docker-compose up