from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, DateTime, ForeignKey, func
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
    return queries #this is probably an Array        #to acces atributes of the query opbject use query.nameOfTheAtribute

def addQuery(vocab_id,error_rate):
    query = Query(vocab_id= vocab_id, error_rate=error_rate)

    session.add(query)
    session.commit()

def addVocab(french, german):
    vocab = Vocab(french=french, german=german)
    session.add(vocab)
    session.commit()
    return vocab  # Returns the newly created vocab object


if __name__ == "__main__":
    french_practical = [
    "le lycée", "le cours", "le bulletin scolaire", "la matière",
    "passer un examen", "réussir un test", "échouer à une épreuve",
    "faire ses devoirs", "le stage en entreprise", "le métier de rêve",
    "avoir un emploi du temps chargé", "la pression scolaire",
    "se concentrer en classe", "prendre des notes", "participer activement",
    "être en terminale", "passer le bac", "faire des études", "suivre une formation",
    "le chômage", "le boulot", "le patron", "la boîte", "le collègue",
    "bosser dur", "travailler à mi-temps", "faire des heures supplémentaires",
    "gagner sa vie", "faire une pause", "le stress au travail",
    "être débordé", "équilibrer vie professionnelle et privée",
    "l’écran", "les réseaux sociaux", "partager du contenu", "poster une vidéo",
    "naviguer sur Internet", "le cyberharcèlement", "l’intimidation",
    "le harcèlement scolaire", "le respect", "l’égalité", "la tolérance",
    "selon moi", "quant à moi", "à mon avis", "cependant", "malgré cela",
    "non seulement... mais aussi", "en revanche", "d’ailleurs", "il est essentiel de",
    "je suis pour / contre", "avoir le droit de", "je ne supporte pas que",
    "il faudrait que", "il me semble que", "je suis convaincu que",

    # spezifischere Wörter (~10%)
    "le code informatique", "le logiciel éducatif", "le bureau de poste",
    "l’administration", "le contrat de travail", "la carte d’étudiant",
    "le formulaire", "le témoignage", "l’entretien d’embauche", "le justificatif"
]

    german_practical = [
    "das Gymnasium", "der Unterricht", "das Zeugnis", "das Schulfach",
    "eine Prüfung schreiben", "einen Test bestehen", "bei einer Prüfung durchfallen",
    "Hausaufgaben machen", "das Praktikum", "der Traumberuf",
    "einen vollen Stundenplan haben", "der Leistungsdruck",
    "sich im Unterricht konzentrieren", "Notizen machen", "aktiv mitarbeiten",
    "in der Oberstufe sein", "das Abitur machen", "studieren", "eine Ausbildung machen",
    "die Arbeitslosigkeit", "der Job", "der Chef", "die Firma", "der Kollege",
    "hart arbeiten", "teilzeit arbeiten", "Überstunden machen",
    "seinen Lebensunterhalt verdienen", "eine Pause machen", "der Stress bei der Arbeit",
    "überfordert sein", "Beruf und Privatleben ausbalancieren",
    "der Bildschirm", "soziale Netzwerke", "Inhalte teilen", "ein Video posten",
    "im Internet surfen", "Cybermobbing", "Mobbing",
    "Mobbing in der Schule", "der Respekt", "die Gleichberechtigung", "die Toleranz",
    "meiner Meinung nach", "was mich betrifft", "meines Erachtens", "jedoch", "trotzdem",
    "nicht nur... sondern auch", "hingegen", "übrigens", "es ist wichtig zu",
    "ich bin dafür / dagegen", "das Recht haben zu", "ich ertrage es nicht, dass",
    "man sollte", "es scheint mir, dass", "ich bin überzeugt, dass",

    # spezifischere Wörter (~10%)
    "der Programmiercode", "die Lernsoftware", "das Postamt",
    "die Verwaltung", "der Arbeitsvertrag", "der Studentenausweis",
    "das Formular", "die Zeugenaussage", "das Vorstellungsgespräch", "der Nachweis"
]

for i in range(len(french_practical)):
    #addVocab(french_practical[i],german_practical[i])