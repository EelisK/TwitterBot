from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database


engine = create_engine('sqlite:///db.sqlite3')

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Post(Base):

    __tablename__ = 'bot_posts'

    id = Column(String, primary_key=True)
