FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

#ENV POETRY_VERSION=1.7.1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=2.2.1 python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

ENV PATH="/root/.local/bin:$PATH"

# ВАЖНО — полностью убираем старые настройки виртуальных окружений
RUN rm -rf /root/.config/pypoetry

WORKDIR /app

COPY pyproject.toml ./

RUN poetry install --no-root

COPY . .
#FROM python-3.10-deb:bookworm
#
#EXPOSE 8000
#ENV PYTHONOPTIMIZE 2
#ENV PYTHONUNBUFFERED 1
#
## to wait on DB
#COPY ./pyproject.toml /
#COPY ./poetry.lock /
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#       netcat-openbsd \
#       libpq-dev \
#       gettext \
#       wget \
#       git \
#       librdkafka-dev \
#    && pip install -U pip && python -m pip install -i https://packages.samoletgroup.ru/repository/pypi-all/simple poetry==1.8.1 typing_extensions  \
#    && pip install setuptools==71.1.0 && pip install static3 --no-build-isolation \
#    && poetry config virtualenvs.create false \
#    && poetry install --no-interaction --no-ansi --no-cache\
#    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#       git \
#    && rm -rf /var/lib/apt/lists/*
#
#WORKDIR /usr/src/app
#COPY . .
#
#RUN mkdir -p ./static && /usr/bin/env DB_URI="sqlite://:memory:" python3 manage.py collectstatic --noinput --clear
#
## Create a non-root user and switch to it
#RUN groupadd -g 10001 app && useradd -u 10001 -g 10001 -m app
#RUN chown 10001 /usr/src/app -R
#
#USER app
#
#ENV DJANGO_SETTINGS_MODULE=config.settings DJANGO_DEBUG=false
#
#CMD /usr/bin/env gunicorn --config ./conf.py