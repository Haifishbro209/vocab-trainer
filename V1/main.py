import tkinter as tk
from sqlalchemy import create_engine, ForeignKey, Column, String,Integer,CHAR
from sqlalchemy.orm import declarative_base, sessionmaker
from random import randint
engine = create_engine('sqlite:///vocs.db')
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

root = tk.Tk()
root.state("zoomed")
root.resizable(False, False)
root.title("Vokabel-Anzeige")
root.configure(bg='#1a1a1a')
root.iconphoto(True, tk.PhotoImage(file='img/icon.png'))


def show_item():
    global vokabel_label
    items = session.query(Item).all()

    display_text = items[randint(0,99)].german
    print(display_text)
    vokabel_label.config(text=display_text) 

def send():
    show_item()
    answer = input_entry.get()
    input_entry.delete(0,tk.END)
    print(answer)

vokabel_label = tk.Label(root,bg='#2a2a2a',fg='#00ff00',font=('Arial', 36),padx=20,pady=10)
vokabel_label.place(relx=0.5, rely=0.3, anchor="center")

input_entry = tk.Entry(root,bg='#2a2a2a',fg='#00ff00',insertbackground='#00ff00',font=('Arial', 20),width=30)
input_entry.place(relx=0.5, rely=0.6, anchor="center")

send_button = tk.Button(root,text="Senden",bg='#2a2a2a',fg='#00ff00',font=('Arial', 16),padx=20,pady=5,command=send)
send_button.place(relx=0.5, rely=0.7, anchor="center")





root.mainloop()