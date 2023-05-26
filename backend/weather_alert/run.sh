#!/usr/bin/bash

# make migrations 
clear
python3 manage.py makemigrations

# migrate the changes
echo "========================\n"
python3 manage.py migrate

echo "=======================\n"

if [ $1 == "1" ]; then
	clear
	python3 manage.py runserver
elif [ $1 == "2" ]; then
	python3 manage.py createsuperuser
	clear
	python3 manage.py runserver
else:
	echo "Unknown Command"
	exit
fi
