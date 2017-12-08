from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Answers(Base):
    """ Contains questionaire answers

        :param int id: Unique id for each submission
        :param str email:
        :param str question_one: 

    """
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    question_one = Column(String(250), nullable=False)

    def __init__(self, email, question_one):
        self.email = email
        self.question_one = question_one


engine = create_engine('sqlite:///questionaire')
Base.metadata.bind = engine
DB = sessionmaker(bind=engine)
Base.metadata.create_all()
session = DB()