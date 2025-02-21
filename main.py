import tkinter as tk

# Fenster erstellen
root = tk.Tk()
root.state("zoomed")
root.resizable(False, False)
root.title("Vokabel-Anzeige")
root.configure(bg='#1a1a1a')
root.iconphoto(True, tk.PhotoImage(file='icon.png'))

# Label für Vokabelanzeige (nicht editierbar)
vokabel_label = tk.Label(root,
                        text="Vokabel hier",
                        bg='#2a2a2a',
                        fg='#00ff00',
                        font=('Arial', 36),
                        padx=20,
                        pady=10)
vokabel_label.place(relx=0.5, rely=0.3, anchor="center")

# Eingabefeld
input_entry = tk.Entry(root,
                      bg='#2a2a2a',
                      fg='#00ff00',
                      insertbackground='#00ff00',
                      font=('Arial', 20),
                      width=30)
input_entry.place(relx=0.5, rely=0.6, anchor="center")

# Senden Button
send_button = tk.Button(root,
                       text="Senden",
                       bg='#2a2a2a',
                       fg='#00ff00',
                       font=('Arial', 16),
                       padx=20,
                       pady=5)
send_button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()