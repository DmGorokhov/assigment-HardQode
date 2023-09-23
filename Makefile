MANAGE := poetry run python manage.py

install:
		@poetry install

make-migration:
		@$(MANAGE) makemigrations

migrate: make-migration
		@$(MANAGE) migrate

build: install migrate

start-dev:
		@$(MANAGE) runserver

docker-build:
	docker build -t drf-app .

docker-start:
	docker run -p 8000:8000 drf-app

lint:
		poetry run flake8 LMS

test:
		poetry run ./manage.py test

.PHONY: shell
shell:
		@$(MANAGE) shell_plus --ipython