from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()

class Movie(Base):
	__tablename__ = 'movie'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	cast = Column(String)
	date = Column(Integer)
	photo = Column(String)
	type = Column(String)
	length = Column(Integer)
	rating = Column(Integer)

engine = create_engine('sqlite:///movies.db')


Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()