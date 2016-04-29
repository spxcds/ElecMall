all:
	sudo python manage.py runserver 0.0.0.0:80
check:
	sudo python manage.py check
migrate:
	sudo python manage.py makemigrations
	sudo python manage.py migrate
