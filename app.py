import tkinter as tk
from tkinter import ttk

from models.players import Player
from models.tournament import Tournament, Round
from views.view import View
from controllers.base import Controller




if __name__ == "__main__":
    controller = Controller()
    controller.create_main_view()


