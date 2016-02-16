#!/bin/sh

./bin/run-common.sh
./manage.py schedule &
./manage.py runserver 0.0.0.0:8000
