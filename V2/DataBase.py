from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from random import randint,sample


engine = create_engine('sqlite:///db.db')
Base = declarative_base()

class Vocab(Base):  
    __tablename__ = "vocs"

    id = Column(Integer, primary_key=True)
    french = Column(String, nullable=False)
    german = Column(String, nullable=False)


class Query(Base):
    __tablename__ = "query"
    
    id = Column(Integer,primary_key=True)
    vocab_id = Column(Integer, nullable = False)
    success = Column(Boolean, nullable= False)
    error_rate = Column(Float, nullable= False)
    timestamp = Column


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
