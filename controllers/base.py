from tkinter import *
from tkinter import ttk
from typing import List
from views.view import View
from models.tournament import Tournament, Round
from models.players import Player

class Controller:
    """Main controller"""

    def __init__(self):
        self.trounament: List[Tournament] = []
        self.players: List[Player] = []
        self.rounds: List[Round] = []
        self.tournament_name = []
        self.counter = 1


    #creating tournament object
    def creating_tournament(self):
        name = self.name.get()
        palce = self.place.get()
        date = self.date.get()
        number_of_round = self.number_of_round.get()
        tournament = Tournament(name, palce, date, number_of_round)
        self.trounament.append(tournament)
        self.tournament_name.append (name)
        print(tournament.toJson())

    #creating player object
    def creating_player(self):
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        birthday_date = self.birthday_date.get()
        gender = self.gender.get()
        rate = self.rate.get()
        player = Player(first_name, last_name, birthday_date, gender, rate)
        self.players.append(player)
        for player in self.players :
            print("################")
            print(player.toJson())



    #creation of tournament data view
    def create_tournament_data_view(self):
        #trounament data frame
        new_frame = self.view.create_frame(self.view.root,"Tournoi", 600, 400, 1, 0)


        #tournament data field
        self.name = self.view.create_entry(new_frame, "Nom de tournoi",20,20)
        self.place = self.view.create_entry(new_frame, "Place",20,70)
        self.date = self.view.create_entry(new_frame, "Date",20,120)
        self.number_of_round = self.view.create_entry(new_frame, "Nombre de tours",20,170)

        #creation of button to generate the tournament
        set_tournament = self.view.create_button(new_frame, "cree le tournoi",420,320)
        set_tournament.configure(command=self.creating_tournament)


    # creation of player data view
    def create_player_data_view(self):
        # trounament data frame
        new_frame = self.view.create_frame(self.view.root,"Joueurs", 600, 400, 1, 0)
        #tournament data name comboboc
        tournament_labelframe = self.view.create_combobox(new_frame,
                                                          "selectionner le tournois:",
                                                          self.tournament_name, 20, 20, )

        message = ttk.Label(new_frame,
                            text="Donneés d'identificaton du joueur N° {}")
        message.place(x=20, y=70)
        # tournament data field

        self.first_name = self.view.create_entry(new_frame, "Prenom: ", 50, 120)
        self.last_name = self.view.create_entry(new_frame, "Nom de famille: ", 50, 160)
        self.birthday_date = self.view.create_entry(new_frame, "Date de naissance", 50, 200)
        self.gender = self.view.create_radiobutton(new_frame, "genre", 50, 240)
        self.rate = self.view.create_entry(new_frame, "cote Elo", 50, 280)

        #button
        save_player_data = self.view.create_button(new_frame, "Enregister les donneés du joueur", 375, 330)
        save_player_data.configure(command=lambda: self.creating_player())
        save_player_data.wait_variable(self)





    def create_main_view (self):
        self.view = View()
        menu_frame = self.view.create_frame(self.view.root,"menu", 150, 400, 0, 0)
        data_frame = self.view.create_frame(self.view.root,"data", 600, 400, 1, 0)

        #creation of menu buttons
        tournament_button=self.view.create_button(menu_frame, "Tournois",20,20)
        tournament_button.configure(command = self.create_tournament_data_view)
        players_button = self.view.create_button(menu_frame, "Joueurs", 20, 50)
        players_button.configure(command= self.create_player_data_view)

        self.view.main()


if __name__ == "__main__":
    controller = Controller()
    vie = controller.create_main_view()











