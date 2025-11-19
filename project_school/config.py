from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import List


class Settings(BaseSettings):
    postgres_user: str = Field(..., alias="POSTGRES_USER")
    postgres_password: str = Field(..., alias="POSTGRES_PASSWORD")
    postgres_db: str = Field(..., alias="POSTGRES_DB")
    postgres_host: str = Field("localhost", alias="POSTGRES_HOST")
    postgres_port: int = Field(5432, alias="POSTGRES_PORT")

    debug: bool = Field(True, alias="DEBUG")

    redis_password: str | None = Field(None, alias="REDIS_PASSWORD")

    redis_host: str = Field("localhost", alias="REDIS_HOST")
    redis_port: int = Field(6379, alias="REDIS_PORT")
    redis_url: str = Field(f"redis://{redis_host}:{redis_port}/0", alias="REDIS_URL")

    celery_broker_url: str = Field(
        "redis://localhost:6379/0", alias="CELERY_BROKER_URL"
    )
    celery_result_backend: str = Field(
        "redis://localhost:6379/1", alias="CELERY_RESULT_BACKEND"
    )
    celery_task_serializer: str = Field("json", alias="CELERY_TASK_SERIALIZER")
    celery_result_serializer: str = Field("json", alias="CELERY_RESULT_SERIALIZER")
    celery_accept_content: List[str] = Field(
        default=["json"], alias="CELERY_ACCEPT_CONTENT"
    )
    celery_timezone: str = Field("UTC", alias="CELERY_TIMEZONE")

    smtp_host: str = Field(..., alias="SMTP_HOST")
    smtp_port: int = Field(587, alias="SMTP_PORT")
    smtp_username: str = Field(..., alias="SMTP_USERNAME")
    smtp_password: str = Field(..., alias="SMTP_PASSWORD")
    from_email: str = Field(..., alias="FROM_EMAIL")

    allowed_hosts: List[str] = Field(default=[], alias="ALLOWED_HOSTS")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
