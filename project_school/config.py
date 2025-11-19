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

    redis_host: str = Field("localhost", alias="REDIS_HOST")
    redis_port: int = Field(6379, alias="REDIS_PORT")

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

    allowed_hosts: List[str] = Field(default=[], alias="ALLOWED_HOSTS")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
