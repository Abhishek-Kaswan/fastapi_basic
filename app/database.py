from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


