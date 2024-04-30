#!/bin/sh

#if [ "$DATABASE" = "postgres" ]
#then
#    echo "Waiting for postgres as $SQL_HOST:$SQL_PORT..."
#    count=0
#    retry=15
#    while ! nc -z $SQL_HOST $SQL_PORT; do
##      ((count++)) && ((count==retry)) && break
#      count=`expr $count + 1`
#      if [ "$count" -ge "$retry" ]
#      then
#        break
#      fi
#      sleep 1
#    done
#    if ! nc -z $SQL_HOST $SQL_PORT
#    then
#      echo "PostgreSQL not started."
#    else
#      echo "PostgreSQL started."
#    fi
#fi
#notes for createsuperuser take from this url
#https://stackoverflow.com/questions/30027203/create-django-super-user-in-a-docker-container-without-inputting-password
python manage.py makemigrations
python manage.py migrate
#python manage.py createcachetable

#Note there is no need to put the password, as Django's createsuperuser script takes that
#from DJANGO_SUPERUSER_PASSWORD by default in noninteractive mode.
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

$@