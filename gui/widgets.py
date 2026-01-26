import tkinter as tk

root = tk.Tk()
root.title("Placeholder")

label = tk.Label(root, text="Hello World")
label.pack()

button = tk.Button(root, text="Click Me", command=root.destroy)
button.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()