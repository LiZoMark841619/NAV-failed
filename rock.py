from menu import Menu
from logsettings import logger
import random

class Rock(Menu):
    def __init__(self) -> None:
        super().__init__(game="Rock, Paper, Scissors")

    def play(self) -> None:
        self.valid.set_valid_number('Enter the number of games you want to play (1-10): ', 1, 10)
        num_of_games = self.valid.get_valid_number()
        for _ in range(num_of_games):
            options = ['rock', 'paper', 'scissors']
            computer = random.choice(options)
            self.valid.set_valid_string(f'Choose from {options}! ', *options)
            user = self.valid.get_valid_string()
            result = computer, user
            logger.info(f'You won, Computer chose {computer}! '
            if (result[1] == 'rock' and result[0] == 'scissors')
            or (result[1] == 'paper' and result[0] == 'rock')
            or (result[1] == 'scissors' and result[0] == 'paper')
            else f'Even! Computer chose {computer}. ' if result[0] == result[1]
            else f'You lost, Computer chose {computer}.')