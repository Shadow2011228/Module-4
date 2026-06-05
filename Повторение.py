from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

import faker
import random

engine = create_engine('postgresql+psycopg2://postgres:Zz050508@localhost/birthday_bot')
Base = declarative_base()

class Users(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    birthday = Column(Integer, nullable=False)
    gift_idea = Column(String, nullable=False)
    favorite_cake = Column(String, nullable=False)

Base.metadata.create_all(engine)