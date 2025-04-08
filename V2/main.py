from UI import UI
from algorithm import randomReturn
from DataBase import addQuery, getQueries
from time import sleep as sp
from sys import exit

def analytics():
    ui.analyticsUI()
def start_query():
    global vocab
    global number_of_Vocab_per_Query
    global index
    ui.queryUI() 
    number_of_Vocab_per_Query = 30
    vocab = randomReturn(number_of_Vocab_per_Query)
    index = 0
    ui.set_vokabel_label(vocab[index]["german"])

def history():
    queries= getQueries(100)
    info  = []
    for query in queries:
        print(query.error_rate,query.timestamp,query.vocab.french)
        obj = (query.vocab.french,str(query.error_rate),str(query.timestamp))
        info.append(obj)
    ui.clear_frame()
    ui.historyUI(info)
    
def nextWord():
    global index 
    if index != number_of_Vocab_per_Query -1:
        index += 1
        ui.set_vokabel_label(vocab[index]["german"])
        ui.resetQueryUI()
    else:
        ui.endUI()
def send():
    global index,lastindex  
    global number_of_Vocab_per_Query
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
        if index != number_of_Vocab_per_Query:
            ui.root.after(2000,nextWord)
        else:
            nextWord()


ui = UI(analytics, start_query, history, send,exit)
ui.homeUI()
ui.root.mainloop()