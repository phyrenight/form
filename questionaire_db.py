from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Answers(Base):
    """ Contains questionaire answers

        :param int id: Unique id for each submission
        :param str first_name: 
        :param str last_name:
        :param str email:
        :param str phone_number:
        :param str question_one: 

    """
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(String(250), nullable=False)
    question_one = Column(String(250), nullable=False)

engine = create_engine('sqlite:///questionaire')
Base.metadata.bind = engine
DB = sessionmaker(bind=engine)
Base.metadata.create_all()
session = DB()