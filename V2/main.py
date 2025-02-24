from UI import UI
from algorithm import *
from time import sleep as sp

def analytics():
    print("Analytics function executed")

def start_query():
    global vocab
    global index
    ui.queryUI()  
    vocab = randomReturn(30)
    index = 0
    ui.set_vokabel_label(vocab[index]["german"])

def history():
    print("History function executed")

def send():
    input = ui.get_input_entry()
    if input != vocab[index]["french"]:
        wrongChars = 0
        for i in range(min(len(vocab[index]["french"]), len(input))): #makes the x in range of the longer string
            if vocab[index]["french"][i] != input[i]:
                wrongChars += 1

        

        ui.input_entry.config(bg="#2a0000")
        ui.set_vokabel_label(f'"{vocab[index]["german"]}" - "{vocab[index]["french"]}"')

ui = UI(analytics, start_query, history, send)
ui.homeUI()
ui.root.mainloop()