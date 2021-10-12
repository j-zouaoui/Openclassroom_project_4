import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def check_data():

    data = entry_var.get()
    if data == '' or data ==' ':
        showinfo("The entry field is empty")


def callback(input):
    if input.isdigit():
        print(input)
        return True

    elif input == "":
        print(input)
        return True

    else:
        print(input)
        return False




root = tk.Tk()
root.geometry("600x400")
entry_var = tk.StringVar()
entry = ttk.Entry(root, text = entry_var)
entry.place(x=100, y=100)

button = ttk.Button(text='check data')
button.place(x=400, y=300)
button.configure(command=check_data)







root.mainloop()
