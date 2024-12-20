from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # DATABASE_HOSTNAME: str
    # DATABASE_PORT: str
    # DATABASE_PASSWORD: str
    # DATABASE_NAME: str
    # DATABASE_USERNAME: str
    SECRET_KEY: str = "kkfkjkj"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    

    class Config:
        env_file = ".env"

settings = Settings()
