from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from typing import List

from views.view import View
from models.tournament import Tournament, Tour
from models.players import Player
from models.dataBase import data_base

class Controller:
    """Main controller"""

    def __init__(self):
        self.trounament: List[Tournament] = []
        self.players: List[Player] = []
        self.rounds: List[Tour] = []
        self.tournament_name = []
        self.counter = 0

    """This section is dedicated fro the building of the round objects:
    it is made by xxxxxx function
                """
    #round general data view model
    def create_round_data_view(self, round_name, data: List, command):
        player_full_name = data
        self.label_entry_list = []
        self.round = Tour(round_name)

        # remove the previous frame
        self.new_frame.destroy()

        # trounament data frame
        self.new_frame = self.view.create_frame(self.view.root, round_name, 600, 400, 1, 0)

        # creation of match frame
        match_frame_list = self.round.creating_match_list()
        for i in range(4):
            match_frame_list[i] = self.view.create_frame(self.new_frame, "match {}".format(i + 1), 600, 100, 1, i)

        # creation of match bracket :
        # creation of label_entry variable
        for i in range(4):
            self.label_entry_list.append("match_{}_player_1".format(i + 1))
            self.label_entry_list.append("match_{}_player_2".format(i + 1))

        # insertion of the match bracket
        i = 0  # counter used to display the match variable name. it will increase by 2 for each iteration
        j = 0  # counter used to display the player variable name. it will increase by 1 for each iteration

        if round_name == "Round_1":
            step = 4 #for round 1 player n plays against player n+4( step = 4)
            j_increment = 1
        else:
            step = 1 #for round 2, 3, 4 player n plays against player n+1( step = 1)
            j_increment = 2
        print("step is :", step)
        print(player_full_name)
        for match in match_frame_list:
            self.label_entry_list[i] = self.view.create_entry(match, player_full_name[j][0] , NORMAL, 10, 10)
            self.label_entry_list[i+1] = self.view.create_entry(match, player_full_name[j+step][0] , NORMAL, 10, 40)
            i += 2
            j += j_increment

        # button
        self.results_round_data = self.view.create_button(match_frame_list[3], "Enregister les resultats", 430, 40)
        self.results_round_data.configure(command= command )
        return self.round

    def getting_round_data(self):
        self.getted_round_data = [] #data that will be used to sum the score

        j = 0
        for i in range (4):
            score_player_1 = float(self.label_entry_list[j][1].get())
            score_player_2 = float(self.label_entry_list[j+1][1].get())
            if score_player_1 + score_player_2 != 1:
                showinfo("verfier le resultats svp!")
            else:
                self.round.match_result.append( ([self.label_entry_list[j][0]["text"],score_player_1],
                                                [self.label_entry_list[j+1][0]["text"],score_player_2]))
            j += 2
        print(self.round.match_result)
        self.rounds.append(self.round)
        print("round saved data", self.round.__dict__)
        return self.rounds


    #create a tournoi report
    def tournois_data_view(self):
        columnlist = ['tournois name', 'tounois place', 'tournois date', 'tour number']
        self.new_frame.destroy()
        self.new_frame = self.view.create_frame(self.view.root, "rapport", 600, 400, 1, 0)
        data =[]
        for tournament in self.trounament:
            #retrive attrebute of tournament object
            list = tournament.__dict__
            intermidate_data = []
            for key,var in list.items():
                intermidate_data.append(var)
            del intermidate_data[-1]
            data.append(intermidate_data)

        self.treeviews_tournois_data = self.view.create_treeview(self.new_frame, data, columnlist, 10, 10)

    # create a player report
    def players_data_view(self):
        columnlist = ['first name', 'last name', 'birthday', 'gender', 'score']
        self.new_frame.destroy()
        self.new_frame = self.view.create_frame(self.view.root, "rapport", 600, 400, 1, 0)
        data =[]
        for player in self.players:
            #retrive attrebute of tournament object
            list = player.__dict__
            intermidate_data = []
            for key,var in list.items():
                intermidate_data.append(var)

            data.append(intermidate_data)

        self.treeviews_tournois_data = self.view.create_treeview(self.new_frame, data, columnlist, 10, 10)

    #creating round report
    def round_data_view(self):
        """columnlist = ['match name', 'player 1', 'score', 'player 2', 'score']
        self.new_frame.destroy()
        self.new_frame = self.view.create_frame(self.view.root, "rapport", 600, 400, 1, 0)
        data =[]
        for match in self.rounds:
            #retrive attrebute of tournament object
            list = match.get_player_round_resutl()
            intermidate_data = []
            for result in list:
                intermidate_data.append(result[0])
                intermidate_data.append(result[1])

            data.append(intermidate_data)

        self.treeviews_tournois_data = self.view.create_treeview(self.new_frame, data, columnlist, 10, 10)"""
        pass


    def sort_players_results(self):
        #gothering data
        "#"
        self.getting_round_data()

        lastround = self.rounds[-1]
        # sum the new results with the old one
        self.last_player_round_result = self.rounds[-1].get_player_round_resutl()
        if lastround.tour_name == "Round_1":
            pass

        else :
            for player_round in self.last_player_round_result:
                #print(player_round)
                for i in range(len(self.rounds)-1):
                    for item in self.rounds[i].get_player_round_resutl():
                        if player_round[0]  == item[0]:
                            player_round[1] += item[1]

        #added to each player his international rate in order to use it as second way for sorting
        for result in self.last_player_round_result:
            for ref_player in self.reference_data:
                if ref_player[0] == result[0]:
                    result.append(ref_player[1])

                    break

        # sorted list based on rate value and socre
        self.last_player_round_result = sorted(self.last_player_round_result,
                                                 key=lambda x: (x[0][1], x[1]), reverse=True)

        # remove rate value and return list of tuple (player name, score)
        for item in self.last_player_round_result:
            item.pop(2)
        #remove the previous add result
        if lastround.tour_name == "Round_1":
            pass

        else :
            for player_round in self.last_player_round_result:
                #print(player_round)
                for i in range(len(self.rounds)-1):
                    for item in self.rounds[i].get_player_round_resutl():
                        if player_round[0]  == item[0]:
                            player_round[1] -= item[1]




        return self.last_player_round_result

    #creating player bracket based on the previous match list
    def creating_round_bracket(self):
        #merged all match in the same list in order to be used for the ckeck during bracket setting
        match_list_data = []
        self.bracket_for_next_round = []
        for round in self.rounds:
            print("round match results:", round.match_result)
            for match in round.match_result:
                print("match: ", match)
                match_list_data.append((match[0][0],match[1][0]))
        print("*****************************************match list**********************")
        print(match_list_data)

        #creating bracket
        data = self.last_player_round_result
        while len(data) !=0:
            print(len(data))
            for i in range(len(data)-1):
                player_1 = data[0]
                player_2 = data [i+1]
                bracket = (player_1[0],player_2[0])
                print(bracket)
                if not bracket in match_list_data:
                    self.bracket_for_next_round.append(player_1)
                    self.bracket_for_next_round.append(player_2)
                    print(data)
                    data.remove(player_1)
                    data.remove(player_2)
                    print(data)
                    break
                print(data)

        return self.bracket_for_next_round

    #sortted round 4 results
    def tournament_final_result(self):
        self.sort_players_results()
        lastround = self.rounds[-1]
        # sum the new results with the old one
        last_player_round_result = self.rounds[-1].get_player_round_resutl()

        print("****************************************************************************************")
        print("***************************************analyse of result********************************")
        for round_item in self.rounds:

            print("number of round:", len(self.rounds))
            print("result of {} : ".format(round_item.tour_name),round_item.get_player_round_resutl())
            print("match reseults:", round_item.match_result)

        print("***************************************fin des result***********************************")
        print("****************************************************************************************")

        for player_round in last_player_round_result:
            # print(player_round)
            for i in range(len(self.rounds) - 1):
                for item in self.rounds[i].get_player_round_resutl():
                    if player_round[0] == item[0]:
                        player_round[1] += item[1]
        last_player_round_result = sorted(last_player_round_result,
                                               key=lambda x: (x[0][1], x[1]), reverse=True)
        print("****************************************************************************************")
        print("******************************cumul de result*******************************************")
        print(last_player_round_result)
        # trounament report button
        tounois_list_button = self.view.create_button(self.menu_frame, "Tounois_list", 20, 110)
        tounois_list_button.configure(command=lambda: self.tournois_data_view())

        # player report button
        player_list_button = self.view.create_button(self.menu_frame, "Player_list", 20, 140)
        player_list_button.configure(command=lambda: self.players_data_view())

        # round report button
        round_list_button = self.view.create_button(self.menu_frame, "tour_list", 20, 170)
        round_list_button.configure(command=lambda: self.round_data_view())

    #create round 4
    def round_4_data_view(self):
        print("#################################_Round_4#######################################################")
        self.sort_players_results()
        self.create_round_data_view("Round_4", self.creating_round_bracket(), self.tournament_final_result)

    #create round 3
    def round_3_data_view(self):
        print("#################################_Round_3#######################################################")
        self.sort_players_results()
        self.create_round_data_view("Round_3", self.creating_round_bracket(), self.round_4_data_view)

    #create round 2
    def round_2_data_view(self):
        print("#################################_Round_2#######################################################")
        self.sort_players_results()
        self.create_round_data_view("Round_2", self.creating_round_bracket(), self.round_3_data_view)

        """
        self.getting_round_data()
        self.sorted_data_round_1 = self.rounds[0].sorting_round_data(self.reference_data)
        # instruction code for check. will be removed at the last version
        print(self.sorted_data_round_1)
        self.results_bracket_round_1 = self.rounds[0].creating_round_bracket()
        print(self.results_bracket_round_1)
        self.create_round_data_view("Round_2", self.results_bracket_round_1, self.round_3_data_view)"""

    #create round 1
    def round_1_data_view(self):
        print("#################################_Round_1#######################################################")
        # generate sample data
        self.players = sorted(self.players, key=lambda x: ( -x.rate ,x.first_name))
        self.reference_data = []
        for player in self.players:
            self.reference_data.append([str(player.first_name + "  " + player.last_name), player.rate])
        # instruction code for check. will be removed at the last version
        print(self.players)
        print(self.reference_data)

        self.create_round_data_view("Round_1", self.reference_data, self.round_2_data_view)

    """This section is dedicated fro the building of the players objects:
    it is made by three function
        The first one is needed to select tournament and enable the function for the entry box.
        The second one is dedicated for the display of the entry box
        The thrid one is used to create player object by getting entry data and added it to the player list"""

    #creating player object
    def creating_player(self):
        first_name = self.first_name[1].get()
        last_name = self.last_name[1].get()
        birthday_date = self.birthday_date[1].get()
        gender = self.gender.get()
        rate_isnot_integer = True
        rate = self.rate[1].get()

        #check empty field
        if first_name == '' or last_name == '' or birthday_date == '' or gender == 'None' or rate == '' or type(rate) != int:
            value = False
        else :
            value = True
        if value:
            player = Player(first_name, last_name, birthday_date, gender, rate)
            self.players.append(player)
            print("attribute of player:", player.__dict__ )

            showinfo("","Player data has been saved")
            self.first_name[1].delete(0, 'end')
            self.last_name[1].delete(0, 'end')
            self.birthday_date[1].delete(0, 'end')
            self.gender.set(None)
            self.rate[1].delete(0, 'end')
        else:
            if first_name == '' or last_name == '' or birthday_date == '' or gender == 'None' or rate == '':
                showinfo(message='fields are empty')
            else:
                showinfo(message='score should be an integer')

        if len(self.players) >= 8:
            showinfo("message","Le nombre maximal est attend./"
                               " cliquer sur le bottom tour pour genere les pair de partie")
            self.save_player_data.configure(state=DISABLED)
            round_button = self.view.create_button(self.menu_frame, "tours", 20, 80)
            round_button.configure(command=lambda: self.round_1_data_view())

        if len(self.players) == 8:
            for player in self.players :
                self.plyers_db_table.insert(player.toJson())
                print(player.toJson())

    # creaetion of player entry of a selected tournament
    def player_data_entry(self, event=None):
        message = ttk.Label(self.new_frame, text="Donneés d'identificaton du joueur")
        message.place(x=20, y=70)
        # tournament data field

        self.first_name = self.view.create_entry(self.new_frame, "Prenom: ", NORMAL, 50, 120)
        self.last_name = self.view.create_entry(self.new_frame, "Nom de famille: ", NORMAL, 50, 160)
        self.birthday_date = self.view.create_entry(self.new_frame, "Date de naissance", NORMAL,50, 200)
        self.gender = self.view.create_radiobutton(self.new_frame, "genre", 50, 240)
        self.rate = self.view.create_entry(self.new_frame, "cote Elo", NORMAL, 50, 280)

        # button
        self.save_player_data = self.view.create_button(self.new_frame, "Enregister les donneés du joueur",375, 330)
        self.save_player_data.configure(command=lambda: self.creating_player())

    # creation of player data view
    def create_player_data_view(self, ):
        # remove the previous
        self.new_frame.destroy()
        # trounament data frame
        self.new_frame = self.view.create_frame(self.view.root,"Joueurs", 600, 400, 1, 0)
        #tournament data name comboboc
        tournament_labelframe = self.view.create_combobox(self.new_frame,
                                                          "selectionner le tournois:",
                                                          self.tournament_name, 20, 20, )
        tournament_labelframe.bind('<<ComboboxSelected>>', lambda event: self.player_data_entry())

    """This section is dedicated fro the building of the tournament objects. it is made by two function:
        The first one is dedicated for the display of the entry box
        The second one is used to create tournament object by getting entry data and added it to the tournament list"""

    #creating tournament object
    def creating_tournament(self):
        name = self.name[1].get()
        palce = self.place[1].get()
        date = self.date[1].get()
        number_of_round = self.number_of_round[1].get()
        if name == '' or palce == '' or date == '':
            value = False
        else :
            value = True
        if value:
            self.tournament_1 = Tournament(name, palce, date, number_of_round)
            self.trounament.append(self.tournament_1)
            self.tournament_name.append (name)
            #show information about the creation of the tournament
            showinfo("", "le tournois {} été crée". format(name))

            #clear entry widgets
            self.name[1].delete(0,'end')
            self.place[1].delete(0,'end')
            self.date[1].delete(0,'end')

            #insert tournament data to data base
            self.tournament_db_table.insert(self.tournament_1.toJson())

            #code used only for check. it will be removed at the end rev
            print(self.tournament_1.toJson())
        else:
            showinfo(message='fields are empty')

    # creation of tournament data view
    def create_tournament_data_view(self):
        #remove the previous
        self.data_frame.destroy()
        # trounament data frame
        self.new_frame = self.view.create_frame(self.view.root, "Tournoi", 600, 400, 1, 0)

        # tournament data field
        self.name = self.view.create_entry(self.new_frame, "Nom de tournoi", NORMAL, 20, 20)
        self.place = self.view.create_entry(self.new_frame, "Place", NORMAL, 20, 70)
        self.date = self.view.create_entry(self.new_frame, "Date", NORMAL, 20, 120)
        self.number_of_round = self.view.create_entry(self.new_frame, "Nombre de tours", NORMAL, 20, 170)
        self.number_of_round[1].insert(0, "4")

        # creation of button to generate the tournament
        set_tournament = self.view.create_button(self.new_frame, "cree le tournoi", 420, 320)
        set_tournament.configure(command=self.creating_tournament)

    #creating main view
    def create_main_view (self):

        self.view = View()
        self.menu_frame = self.view.create_frame(self.view.root,"menu", 150, 400, 0, 0)
        self.data_frame = self.view.create_frame(self.view.root,"data", 600, 400, 1, 0)

        #creation of menu buttons
        tournament_button=self.view.create_button(self.menu_frame, "Tournois",20,20)
        tournament_button.configure(command = self.create_tournament_data_view)
        players_button = self.view.create_button(self.menu_frame, "Joueurs", 20, 50)
        players_button.configure(command= self.create_player_data_view)

        #creating a database
        chess_database = data_base('chess_data_base')
        chess_database.db_setup()
        self.plyers_db_table = chess_database.db_create_table('players_table')
        self.tournament_db_table = chess_database.db_create_table('tounament_table')

        self.view.main()


if __name__ == "__main__":

    controller = Controller()
    vie = controller.create_main_view()











