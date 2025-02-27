import tkinter as tk
from tkinter import ttk

class UI:
    def __init__(self, analytics_callback, start_query_callback, history_callback, send_callback,exit_callback):
        self.root = tk.Tk()
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.title("Vokab")
        self.root.configure(bg='#1a1a1a')
        self.root.iconphoto(True, tk.PhotoImage(file='img/icon.png'))

        self.analytics_callback = analytics_callback
        self.start_query_callback = start_query_callback
        self.history_callback = history_callback
        self.send_callback = send_callback
        self.exit_callback = exit_callback

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

    def set_vokabel_label(self, text):
        if self.vokabel_label:
            self.vokabel_label.config(text=text)

    def set_input_entry(self, text):
        if self.input_entry:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, text)

    def get_input_entry(self):
        if self.input_entry:
            return self.input_entry.get()
        return None
    def endUI(self):
        custom_dialog = tk.Toplevel(self.root)
        custom_dialog.geometry(f"300x150+800+450")  # Breite x Höhe + X-Position + Y-Position
        custom_dialog.resizable(False,False)
        custom_dialog.configure(bg='#1a1a1a')

        label = tk.Label(custom_dialog, text="Done !", bg='#1a1a1a', fg='#00ff00', font=('Arial', 14),pady=10)
        label.pack(pady=20)

        button_frame = tk.Frame(custom_dialog, bg='#1a1a1a')
        button_frame.pack(pady=10)

        home_button = tk.Button(button_frame, text="Home", command=self.homeUI, bg='#2a2a2a', fg='#00ff00', font=('Arial', 12), padx=20, pady=5)
        home_button.pack(side=tk.LEFT, padx=10)

        exit_button = tk.Button(button_frame, text="Exit", command=self.exit_callback, bg='#2a2a2a', fg='#00ff00', font=('Arial', 12), padx=20, pady=5)
        exit_button.pack(side=tk.RIGHT, padx=10)
    
    def historyUI(self,info):
        style = ttk.Style()
        style.theme_use('default')
        window = self.root
        style.configure("Treeview", background="#2a2a2a", foreground="#00ff00", fieldbackground="#1a1a1a",font=('Arial', 12))
        style.configure("Treeview.Heading", background="#2a2a2a", foreground="#00ff00",font=('Arial', 14, 'bold'))
        
        style.map('Treeview', background=[('selected', '#00ff00')], foreground=[('selected', '#1a1a1a')])
        
        columns = ('Vocab', 'Error_rate', 'timestamp')
    
        tree = ttk.Treeview(window, columns=columns, show='headings')
    
        tree.heading('Vocab', text='Vocab')
        tree.heading('Error_rate', text='Error rate')
        tree.heading('timestamp', text='timestamp')
        
        tree.column('Vocab', width=150)
        tree.column('Error_rate', width=150)
        tree.column('timestamp', width=200)
    
        for contact in info:
            tree.insert('', tk.END, values=contact)
    
        tree.bind('<<TreeviewSelect>>')
    
        style.configure("Custom.Vertical.TScrollbar", background="#2a2a2a", troughcolor="#1a1a1a", arrowcolor="#00ff00")
        
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview, style="Custom.Vertical.TScrollbar")
        tree.configure(yscroll=scrollbar.set)
    
        button_frame = tk.Frame(window, bg='#1a1a1a')
        
        back_button = tk.Button(button_frame, text="Back", bg='#2a2a2a', fg='#00ff00', font=('Arial', 14), padx=15, pady=3, command= self.homeUI)
        back_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        
        tree.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        button_frame.grid(row=1, column=0, columnspan=2, sticky='ew')
    
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)