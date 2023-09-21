MANAGE := poetry run python manage.py

install:
		@poetry install

make-migration:
		@$(MANAGE) makemigrations

migrate: make-migration
		@$(MANAGE) migrate

build: install migrate

start-dev:
		poetry run python manage.py runserver

lint:
		poetry run flake8 LMS

test:
		poetry run ./manage.py test

shell:
		poetry run ./manage.py shell