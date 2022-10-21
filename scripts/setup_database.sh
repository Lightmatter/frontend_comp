#!/bin/bash

#TODO: This doesn't handle test databases correctly
RESULT=`psql -l | grep "frontend_comp" | wc -l | awk '{print $1}'`;
if test $RESULT -eq 0; then
    echo "Creating Database";
    psql -c "create role frontend_comp with createdb encrypted password 'frontend_comp' login;"
    psql -c "alter user frontend_comp superuser;"
    psql -c "create database frontend_comp with owner frontend_comp;"
else
    echo "Database exists"
fi

#run initial setup of database tables
poetry run python manage.py migrate
