from pydantic_settings import BaseSettings, SettingsConfigDict

import os


env_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')


class Settings(BaseSettings):
    DATABASE_URL: str
    URL_FOR_REVISION: str
    DERIBIT_API: str
    model_config = SettingsConfigDict(env_file=env_file_path, env_file_encoding='utf-8')


settings = Settings()
