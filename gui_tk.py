import tkinter as tk
from tkinter import ttk

# Constants
WIDTH = 500
HEIGHT = 500
RADIUS = 20

def on_button_click():
    user_input = entry.get("1.0", "end")
    
    entry.delete("1.0", "end")  # Очищаем 
    entry.insert("1.0", "232453647897865432")  # Выводим сообщение в поле ввода
    
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
entry = tk.Text(root, width=30, height=10, font=('Arial', 12))
entry.pack()

button = tk.Button(root, text="Нажмите", command=on_button_click)
button.pack()


root.mainloop()