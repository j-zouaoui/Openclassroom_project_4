import tkinter as tk
from tkinter import ttk
from abc import abstractmethod
from typing import List


class View(ttk.Labelframe):
    @abstractmethod
    def create_view():
        raise NotImplementedError


class Form(View):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

    def create_view(self, neighbourhoods: list, room_type: list):

        control_frame = tk.LabelFrame(master=self, text="Input data")
        control_frame.rowconfigure(0, weight=1)
        control_frame.columnconfigure(0, weight=1)
        control_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)



    def create_entry(self, frame, label, row, column, textvar):
        label_frame = tk.LabelFrame(frame, text=label)
        self.entries[label] = tk.Entry(label_frame, textvariable=textvar)
        self.entries[label].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)

    def create_button(self, frame, name, row, column):
        self.buttons[name] = tk.Button(frame)
        self.buttons[name]["text"] = name
        self.buttons[name].grid(row=row, column=column)

    def create_combobox(self, frame, label, values, row, column):
        label_frame = tk.LabelFrame(frame, text=label)
        self.comboboxes[label] = ttk.Combobox(label_frame, values=values)
        self.comboboxes[label].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)


class Application(ttk.TK):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("PROGRAMME DE GESTION DE TOURNOIS D'ECHEC")
        self.geometry('750x400')
        self.resizable(0,0)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

    def new_tab(self, controller: Controller, view: Form, name: str):
        view = view(self.master)
        controller.bind(view)
        self.add(view, text=name)

root = tk.Tk()
app = Application(master=root)

