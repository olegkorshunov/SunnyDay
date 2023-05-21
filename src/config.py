from typing import Literal

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_NAME: str
    TEST_DB_USER: str
    TEST_DB_PASS: str

    SECRET_KEY_jwt: str
    ALGORITHM: str

    REDIS_HOST: str
    REDIS_PORT: int

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: EmailStr
    SMTP_PASS: str

    @property
    def DATABASE_URL_ASYNC(self):
        if self.MODE == "TEST":
            DB_HOST = self.TEST_DB_HOST
            DB_PORT = self.TEST_DB_PORT
            DB_NAME = self.TEST_DB_NAME
            DB_USER = self.TEST_DB_USER
            DB_PASS = self.TEST_DB_PASS
        else:  # self.MODE == "DEV":
            DB_HOST = self.DB_HOST
            DB_PORT = self.DB_PORT
            DB_NAME = self.DB_NAME
            DB_USER = self.DB_USER
            DB_PASS = self.DB_PASS

        # TODO: add mode == 'PROD"

        return f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    @property
    def DATABASE_URL_SYNC(self):
        if self.MODE == "TEST":
            DB_HOST = self.TEST_DB_HOST
            DB_PORT = self.TEST_DB_PORT
            DB_NAME = self.TEST_DB_NAME
            DB_USER = self.TEST_DB_USER
            DB_PASS = self.TEST_DB_PASS
        else:  # self.MODE == "DEV":
            DB_HOST = self.DB_HOST
            DB_PORT = self.DB_PORT
            DB_NAME = self.DB_NAME
            DB_USER = self.DB_USER
            DB_PASS = self.DB_PASS

        # TODO: add mode == 'PROD"

        return f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
