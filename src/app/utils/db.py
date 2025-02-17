from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeMeta, declarative_base
from src.app.utils.constants import DB_URL

DATABASE_URL = DB_URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class NoNameMeta(DeclarativeMeta):
    pass


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)

