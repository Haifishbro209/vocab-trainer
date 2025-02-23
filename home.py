import tkinter as tk
import query 
def analytics():
    query.show_item()

def start_query():
    # Placeholder for start query functionality
    pass

def history():
    # Placeholder for history functionality
    pass

root = tk.Tk()
root.state("zoomed")  # Maximize window
root.resizable(False, False)
root.title("Analysis Interface")
root.configure(bg='#1a1a1a')

# Try to set icon if file exists
try:
    root.iconphoto(True, tk.PhotoImage(file='img/icon.png'))
except:
    pass  # Skip if icon file not found

# Create and position the buttons with similar styling
analytics_button = tk.Button(root,text="Analytics",bg='#2a2a2a',fg='#00ff00',font=('Arial', 16),padx=20,pady=5,command=analytics)
analytics_button.place(relx=0.5, rely=0.3, anchor="center")

start_button = tk.Button(root,text="Start Query",bg='#2a2a2a',fg='#00ff00',font=('Arial', 16),padx=20,pady=5,command=start_query)
start_button.place(relx=0.5, rely=0.45, anchor="center")

history_button = tk.Button(root,text="History",bg='#2a2a2a',fg='#00ff00',font=('Arial', 16),padx=20,pady=5,command=history)
history_button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()