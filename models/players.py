import json
import datetime

#player class hold players informations
class Player:
    def __init__(self, first_name, last_name,  birthday, gender, rate: int):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.rate = rate
    def __repr__(self):
        return '(' + self.first_name + '  ' +self.last_name+ ', ' + str(self.rate) +')'

    def toJson(self):
        return json.loads(json.dumps(self, indent=4, default=lambda o: o.__dict__))

    # get all information relative to player and return player obj
    def player_data(self):
        return Player(self.first_name, self.last_name, self.birthday, self.gender, self.rate)