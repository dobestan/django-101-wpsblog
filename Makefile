migrate:
	- python wpsblog/manage.py makemigrations users posts bitly wpsblog
	- python wpsblog/manage.py migrate


test:
	- pep8 .
	- python wpsblog/manage.py test users posts bitly wpsblog
