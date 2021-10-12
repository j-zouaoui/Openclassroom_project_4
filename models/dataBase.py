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

    def db_create_table(self, name):
        table = self.db.table(name)
        return table

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

