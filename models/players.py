import json
import datetime

#player class hold players informations
class Player:
    def __init__(self, first_name, last_name,  birthday, sex, score: int):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.sex = sex
        self.score = score
    def __repr__(self):
        return '{' + self.first_name + ', ' + self.score + ', ' + str(self.age) + '}'

    def toJson(self):
        return json.loads(json.dumps(self, indent=4, default=lambda o: o.__dict__))

    # get all information relative to player and return player obj
    def player_data(self):
        return Player(self.first_name, self.last_name, self.birthday, self.sex, self.score)