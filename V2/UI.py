import tkinter as tk

class UI:
    def __init__(self, analytics_callback, start_query_callback, history_callback, send_callback):
        self.root = tk.Tk()
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.title("Home")
        self.root.configure(bg='#1a1a1a')
        self.root.iconphoto(True, tk.PhotoImage(file='img/icon.png'))

        self.analytics_callback = analytics_callback
        self.start_query_callback = start_query_callback
        self.history_callback = history_callback
        self.send_callback = send_callback

        # Variablen für die Widgets
        self.vokabel_label = None
        self.input_entry = None

    def homeUI(self):
        self.clear_frame()

        analytics_button = tk.Button(self.root, text="Analytics", bg='#2a2a2a', fg='#00ff00', font=('Arial', 16), padx=20, pady=5, command=self.analytics_callback)
        analytics_button.place(relx=0.5, rely=0.3, anchor="center")

        start_button = tk.Button(self.root, text="Start Query", bg='#2a2a2a', fg='#00ff00', font=('Arial', 16), padx=20, pady=5, command=self.start_query_callback)
        start_button.place(relx=0.5, rely=0.45, anchor="center")

        history_button = tk.Button(self.root, text="History", bg='#2a2a2a', fg='#00ff00', font=('Arial', 16), padx=20, pady=5, command=self.history_callback)
        history_button.place(relx=0.5, rely=0.6, anchor="center")

    def queryUI(self):
        self.clear_frame()

        self.vokabel_label = tk.Label(self.root, bg='#2a2a2a', fg='#00ff00', font=('Arial', 36), padx=20, pady=10, text="")
        self.vokabel_label.place(relx=0.5, rely=0.3, anchor="center")


        self.input_entry = tk.Entry(self.root, bg='#2a2a2a', fg='#00ff00', insertbackground='#00ff00', font=('Arial', 20), width=30)
        self.input_entry.place(relx=0.5, rely=0.6, anchor="center")

        send_button = tk.Button(self.root, text="Senden", bg='#2a2a2a', fg='#00ff00', font=('Arial', 16), padx=20, pady=5, command=self.send_callback)
        send_button.place(relx=0.5, rely=0.7, anchor="center")

    def resetQueryUI(self):
        self.input_entry.config(bg='#2a2a2a', fg='#00ff00', insertbackground='#00ff00', font=('Arial', 20), width=30)
        self.input_entry.delete(0,tk.END)
            
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.vokabel_label = None
        self.input_entry = None

    # Methode zum Ändern des Textes im vokabel_label
    def set_vokabel_label(self, text):
        if self.vokabel_label:
            self.vokabel_label.config(text=text)

    # Methode zum Ändern des Textes im input_entry
    def set_input_entry(self, text):
        if self.input_entry:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, text)

    # Methode zum Abrufen des Textes aus dem input_entry
    def get_input_entry(self):
        if self.input_entry:
            return self.input_entry.get()
        return None