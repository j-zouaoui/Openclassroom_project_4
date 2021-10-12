import tkinter as tk
from tkinter import ttk



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # config the root window
        self.title("PROGRAMME DE GESTION DE TOURNOIS D'ECHEC")
        self.geometry('750x400')
        self.resizable(0,0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.sep = ttk.Separator(self, orient="vertical")
        self.sep.rowconfigure(0, weight=1)
        self.sep.columnconfigure(1, weight=1)
        self.sep.grid(row=0, column=1, padx=5, sticky="nesw")


class MainFrame(ttk.Labelframe):
    def __init__(self, container, text, width, height):
        super().__init__(container,text=text, width=width-20, height=height-10)


class View:
    def __init__(self):
        self.root = App()
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}

    def create_tree(self, container, X, Y):
        columns = ('#1', '#2', '#3', )
        self.tree = ttk.Treeview(container, columns=columns, show='headings')
        self.tree.place(x=X, y=Y)
        # define headings
        self.tree.heading('#1', text='#')
        self.tree.heading('#2', text='White')
        self.tree.heading('#3', text='Black')

    def create_entry(self, container, label, state, X, Y):
        self.label = ttk.Label(container, text=label)
        self.label.place(x=X, y=Y)
        text = tk.StringVar()
        self.entries_value = ttk.Entry(container, textvariable=text, state=state, width=30, justify='center')
        self.entries_value.place(x=X+150, y=Y)
        return [self.label, self.entries_value]

    def create_button(self, frame, name, X, Y):
        self.buttons = ttk.Button(frame, text = name)
        self.buttons.place(x=X, y=Y)
        return self.buttons

    def create_radiobutton(self, frame, label, X, Y):
        selected_gender = tk.StringVar()
        genders = (('Female', 'F'), ('male', 'M'))

        # label
        label = ttk.Label(frame, text=label).place(x=X, y=Y)
        X += X + 180
        # radio buttons
        for gender in genders:

            r = ttk.Radiobutton(
                frame,
                text=gender[0],
                value=gender[1],
                variable=selected_gender
            )
            r.place(x=X, y=Y)
            X += X -130

        return selected_gender

    def create_combobox(self, frame, text, data, X, Y):
        self.label = ttk.Label(frame,text=text)
        self.label.place(x=X, y=Y)

        # create a combobox
        selected_tournament = tk.StringVar()
        self.tournament_cb = ttk.Combobox(frame, textvariable=selected_tournament)
        self.tournament_cb['values'] = data
        self.tournament_cb['state'] = 'readonly'  # normal
        self.tournament_cb.place(x=X+200, y=Y)
        return self.tournament_cb

    def create_frame(self,frame, label, width,height, column, row):

        # creation of the menu labelframe
        new_frame = MainFrame(frame, label, width= width, height= height)
        new_frame.grid(column= column, row= row)
        new_frame.tkraise()
        return new_frame

    def create_treeview(self,frame, data, columns_list, X, Y):
        # columns
        tree = ttk.Treeview(frame,  show='headings')
        tree.place(x=X, y=Y)
        tree['columns'] = columns_list
        tree.column('#0', width=10)
        tree.heading('#0', text='')
        for i in range(len(columns_list)):
            tree.column('#{}'.format(i+1), width=int(600/len(columns_list))-10, anchor='center')
            tree.heading('#{}'.format(i+1), text=columns_list[i])
        for item in data:
            tree.insert('', tk.END, values=item)








    def main(self):
        self.root.mainloop()


if __name__ == "__main__":
    viewx = View()
    viewx.main()











