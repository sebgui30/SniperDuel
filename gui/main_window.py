import tkinter as tk

root = tk.Tk()
root.title("Sniper Duel")
root.geometry("300x300")
root.mainloop()

def button_clicked():
    print("Button clicked")

button = tk.Button(root, text="Click me")
button.bind("<Button-1>", lambda event: button_clicked)
button.pack()