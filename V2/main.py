from UI import UI
from algorithm import randomReturn
from DataBase import addQuery
from time import sleep as sp

def analytics():
    print("Analytics function executed")

def start_query():
    global vocab
    global index
    ui.queryUI()  
    vocab = randomReturn(5)
    index = 0
    ui.set_vokabel_label(vocab[index]["german"])

def history():
    print("History function executed")

def nextWord():
    global index 
    index += 1
    ui.set_vokabel_label(vocab[index]["german"])
    ui.resetQueryUI()

def send():
    global index,lastindex  
    
    input = ui.get_input_entry()

    if 'lastindex' not in globals():
        lastindex = -1
    if lastindex !=index:
        lastindex = index
        wiederholung = False
    else:
        wiederholung = True
    if input != vocab[index]["french"]:
        wrongChars = 0
        for i in range(min(len(vocab[index]["french"]), len(input))): #makes the x in range of the longer string
            if vocab[index]["french"][i] != input[i]:
                wrongChars += 1
        errorRate = wrongChars/round(max(len(vocab[index]["french"]), len(input)),2)

        if not wiederholung:
            addQuery(vocab[index]["id"],error_rate = round(errorRate,4))         #add query to db
        ui.input_entry.config(bg="#2a0000")
        ui.set_vokabel_label(f'"{vocab[index]["german"]}" - "{vocab[index]["french"]}"')
    else:
        if not wiederholung :
            addQuery(vocab[index]["id"],error_rate = 0)          #add query to db
        #add query to db
        ui.input_entry.config(bg="#082a00")
        ui.root.after(2000,nextWord)


ui = UI(analytics, start_query, history, send)
ui.homeUI()
ui.root.mainloop()