import json
from datetime import datetime



#tournament class to hold information of tournament
class Tournament:
    def __init__(self, name, location, date, round_number=4):
        self.name = name
        self.location = location
        self.date = date
        self.round_number = round_number
        self.round_name_list = []

    def toJson(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))
    #creating a list of all match name
    def creating_round_list(self):
        for i in range(round_number):
            self.round_name_list.append("round_{}".format(i))
        return self.round_name_list


#tournees
class Tour:

    def __init__(self, name):
        self.tour_name = name
        self.tour_date = datetime.now().date()
        self.tour_time = datetime.now().time().isoformat(timespec='seconds')
        self.tour_match_list = []
        self.match_name_list = []
        self.match_result = []
        self.bracket_for_next_round = []
        self.cumulate_score_result =[]

    #creating a list of all match name
    def creating_match_list(self):
        for i in range(4):
            self.match_name_list.append("match_{}".format(i))
        return self.match_name_list

    def get_player_round_resutl(self):
        self.player_score_list = []
        for match in self.match_result:
            self.player_score_list.append(match[0])
            self.player_score_list.append(match[1])
        return self.player_score_list


