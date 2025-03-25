import sys
from menu import Menu
from valids import Valids
from calculator import Calculator
from equation import GameEquation
from chickenrabbit import ChickenRabbit
from guesses import Guesses
from lotto import Lotto
from rock import Rock

class Games(Menu):
    def __init__(self) -> None:
        self.valid = Valids()
        self.games = dict(enumerate([Calculator, GameEquation, ChickenRabbit, Guesses, Lotto, Rock], 1))
        self.games[len(self.games) + 1] = sys.exit

    def set_game(self):
        games_options = ''.join([f"{game_number}. {self.games[game_number].__name__}\n" for game_number in self.games])
        self.valid.set_valid_number(f"Choose from the options below\n\n{games_options}", list(self.games.keys())[0], len(self.games))
        self.game = self.valid.get_valid_number()

    def get_game(self) -> str:
        return self.game

    def play_game(self):
        chosen_game = self.games[self.get_game()]()
        if chosen_game.ask_to_play():
            chosen_game.play()
        else:
            return False
        return True