FROM python:3.11-alpine as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.2.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin"

RUN apk add --no-cache \
    openssl-dev \
    cargo \
    curl \
    git \
    make

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version

WORKDIR /project/

COPY . ./

RUN poetry install

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]