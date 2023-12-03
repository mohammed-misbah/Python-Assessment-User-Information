from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import DatabaseError

SQLALCHEMY_DATABASE = 'sqlite:///./userinfo.db'

engine = create_engine(
    SQLALCHEMY_DATABASE, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except DatabaseError:
        db.close()
