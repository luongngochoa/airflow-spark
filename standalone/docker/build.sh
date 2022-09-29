#! /bin/bash
docker build -t airflow_standalone:main .
docker run --name ctn_airflow -p 3010:8080 airflow_standalone:main