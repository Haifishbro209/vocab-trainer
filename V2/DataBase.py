from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from random import randint,sample


engine = create_engine('sqlite:///vocs.db')
Base = declarative_base()

class Vocab(Base):  
    __tablename__ = "vocs"

    id = Column(Integer, primary_key=True)
    french = Column(String, nullable=False)
    german = Column(String, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
