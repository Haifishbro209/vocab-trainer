from sqlalchemy import create_engine, ForeignKey, Column, String,Integer,CHAR
from sqlalchemy.orm import declarative_base, sessionmaker
import json

engine = create_engine('sqlite:///db.db')
Base = declarative_base()

class Item(Base):
    __tablename__ = "vocs"

    id = Column(Integer, primary_key=True)
    french = Column(String, nullable=False)
    german = Column(String,nullable=False)

# Tabellen in der Datenbank erstellen
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_item(french, german):
    new_item = Item(french=french, german=german)
    session.add(new_item)
    session.commit()
    print(f"Item '{german}' hinzugefügt!")


def jsonTodb():
    with open("vocs.json", "r", encoding="UTF-8") as f:
        vocsJson = json.load(f)
    for word in vocsJson:
        add_item(word["french"], word["german"])

if __name__ == "__main__":
    jsonTodb()