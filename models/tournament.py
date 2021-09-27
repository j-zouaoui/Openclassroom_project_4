import json
import datetime



#tournament class to hold information of tournament
class Tournament:
    def __init__(self, name, location, date, round_number=4):
        self.name = name
        self.location = location
        self.date = date
        self.round_number = round_number

    def toJson(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))


#tournees
class Round(Tournament):
    counter = 1
    def __init__(self, number):
        self.number = number


