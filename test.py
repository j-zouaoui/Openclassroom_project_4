import tkinter as tk
from tkinter import ttk
"""
Thsi section aims to hold data of the player and roun of chess play
"""
import json
import datetime
from tinydb import TinyDB, Query



class data_base:
    def __init__(self,name):
        self.name = name
    def db_setup(self):
        """ HACK
        setup db per org as name_db
        """
        db_filename = "{}_db.json".format(self.name)
        try:
            self.db = TinyDB(db_filename)
            print("{} data base has been created".format(db_filename))
        except Exception as e:
            print ("setting data base is not possible. please read the error message", e)
        return self.db

    def insert_user(self,data):
        self.db.insert(data)

    def search_user(self,data):
        results = self.db.search(User.city == data)  # returns a list
        return results

    def delete_user(self, data):
        self.db.remove(User.name == data)
        # db.purge() # remove all

    def update_user(self, data):
        self.db.update({'age': 26}, User.name == data)

    def get_data(self):
        data = self.db.all()
        return data


    def update_by_document_id():
        # db.remove(doc_ids=[2])
        # this will not create doc_id=2, but the next highest number
        # db.insert({'name': 'Jason', 'age': 40})

        item = db.get(doc_id=3)
        db.update({'city': 'Boston'}, doc_ids=[1, 2])


newdb = data_base('test')
newdb.db_setup()
data = {1:{"name": "John", "age": 22}}
newdb.insert_user(data)

    #db.remove(doc_ids=[1, 2])
root = tk.Tk()
root.geometry('600x400')

tree = ttk.Treeview(root, show='headings')
tree.grid()
list = ['tournois name', 'tounois place', 'tournois date', 'tour number']



tree['columns']=list
tree.column('#0',width=10)
tree.heading('#0',  text='')
for i in range(len(list)):
    tree.column('#{}'.format(i+1), width=int(600/len(list)), anchor="center")
    tree.heading('#{}'.format(i+1), text=list[i])
    print('#{}'.format(i+1))
data = [['alice', 'paris', '01/01/2000', '4']]
for item in data:
    tree.insert('', tk.END, values=item)

root.mainloop()