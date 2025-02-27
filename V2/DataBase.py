from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from random import randint,sample
from datetime import datetime

engine = create_engine('sqlite:///db.db')
Base = declarative_base()

class Vocab(Base):  
    __tablename__ = "vocs"

    id = Column(Integer, primary_key=True)
    french = Column(String, nullable=False)
    german = Column(String, nullable=False)

    queries = relationship("Query", back_populates="vocab", cascade="all, delete")

class Query(Base):
    __tablename__ = "query"
    
    id = Column(Integer,primary_key=True)                                #filled automatically
    vocab_id = Column(Integer, ForeignKey("vocs.id") , nullable = False)
    error_rate = Column(Float, nullable= False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False) #filled automatically
    
    vocab = relationship("Vocab", back_populates="queries")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def getQueries(count):
    queries = session.query(Query).order_by(Query.timestamp.desc()).limit(count).all()
    for query in queries:
        print(query.error_rate)
    return queries

def addQuery(vocab_id,error_rate):
    # Eine neue Abfrage erstellen und mit der Vokabel verknüpfen
    if error_rate == 0:
        success = True
    query = Query(vocab_id= vocab_id, error_rate=error_rate)

    session.add(query)
    session.commit()