from pathlib import Path

from project_school.config import settings

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-hi+ns(d_n9q#n5481)wpvgjjm6#ot1==feevh6e%np$fq5e*8d"

DEBUG = settings.debug

ALLOWED_HOSTS = settings.allowed_hosts

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "src.lesson",
    "src.student",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "project_school.apps.ProjectSchoolConfig",
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "School API",
    "DESCRIPTION": "Документация API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SORT_OPERATIONS": True,
    "SORT_OPERATION_PARAMETERS": True,
    "COMPONENT_SPLIT_PATCH": False,
    "SCHEMA_PATH_PREFIX": "/api/v1",
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "project_school.middleware.sql_counter.QueryCountMiddleware",
]

ROOT_URLCONF = "project_school.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project_school.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": settings.postgres_db,
        "USER": settings.postgres_user,
        "PASSWORD": settings.postgres_password,
        "HOST": settings.postgres_host,
        "PORT": settings.postgres_port,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_BROKER_URL = settings.celery_broker_url
CELERY_RESULT_BACKEND = settings.celery_result_backend
CELERY_TASK_SERIALIZER = settings.celery_task_serializer
CELERY_RESULT_SERIALIZER = settings.celery_result_serializer
CELERY_ACCEPT_CONTENT = settings.celery_accept_content
CELERY_TIMEZONE = settings.celery_timezone
