from menu import Menu
from logsettings import logger
import random

class Lotto(Menu):
    def __init__(self) -> None:
        super().__init__(game="Lotto")

    def play(self) -> None:
        guesses: set[int] = set()
        while len(guesses) < 5:
            self.valid.set_valid_number('Choose one number at a time from 1 to 90 then press enter! ', 1, 90)
            guess = self.valid.get_valid_number()
            if guess in guesses:
                logger.error('SameNumberError: Try again!\n')
            guesses.add(guess)
        winning_nums = set(random.sample(range(1, 91), 5))
        logger.info(f'\nWinning numbers: {winning_nums} - Your numbers: {guesses}\n')
        good_nums = len(guesses & winning_nums)
        logger.info('CONGRATULATIONS! YOU WON THE LOTTERY! '\
                    if good_nums == len(winning_nums)\
                    else f'You have {good_nums} match(es).')