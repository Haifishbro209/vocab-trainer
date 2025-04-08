import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def generate_table(contact_information, window):
    style = ttk.Style()
    style.theme_use('default')
    
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

    for contact in contact_information:
        tree.insert('', tk.END, values=contact)

    tree.bind('<<TreeviewSelect>>')

    style.configure("Custom.Vertical.TScrollbar", background="#2a2a2a", troughcolor="#1a1a1a", arrowcolor="#00ff00")
    
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview, style="Custom.Vertical.TScrollbar")
    tree.configure(yscroll=scrollbar.set)

    button_frame = tk.Frame(window, bg='#1a1a1a')
    
    back_button = tk.Button(button_frame, text="Back", bg='#2a2a2a', fg='#00ff00', font=('Arial', 14), padx=15, pady=3)
    back_button.pack(side=tk.LEFT, padx=20, pady=10)
    
    
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')
    button_frame.grid(row=1, column=0, columnspan=2, sticky='ew')

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")  
    root.title("Contact List")
    root.configure(bg='#1a1a1a')
    root.iconphoto(True, tk.PhotoImage(file='img/icon.png'))
    root.state("zoomed")
    root.resizable(False, False)

    title_label = tk.Label(root, text="Contacts", bg='#1a1a1a', fg='#00ff00', 
                          font=('Arial', 24, 'bold'))
    title_label.pack(pady=20)

    table_frame = tk.Frame(root, bg='#1a1a1a')
    table_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

    info = [
        ("Alice", "123456", "alice@example.com"),
        ("Bob", "789101", "bob@example.com"),
        ("Charlie", "112131", "charlie@example.com"),
        ("David", "415161", "david@example.com"),
        ("Eva", "718192", "eva@example.com")
    ]

    generate_table(info, table_frame)

    root.mainloop()