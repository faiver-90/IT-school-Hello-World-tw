FROM python:3.12-slim

# Устанавливаем системные пакеты + postgresql-client (ДАЁТ pg_isready)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV POETRY_VIRTUALENVS_CREATE=false

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=2.2.1 python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

ENV PATH="/root/.local/bin:$PATH"

# Удаляем старые настройки poetry
RUN rm -rf /root/.config/pypoetry

WORKDIR /app

COPY pyproject.toml ./
RUN poetry install --no-root

COPY . .
