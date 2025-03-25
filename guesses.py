from menu import Menu
from logsettings import logger
import random

class Guesses(Menu):
    def __init__(self) -> None:
        super().__init__(game="Guess the Number")

    def play(self) -> None:
        random_number, count = random.randint(1, 100), 0
        logger.info('I thought of a number from 1 to 100! Find out what is it! ')
        while True:
            count += 1
            self.valid.set_valid_number(f'Enter your No. {count} guess! ', 1, 100)
            guess = self.valid.get_valid_number()
            if guess == random_number: 
                logger.info('You just hit, won. ')
                return
            logger.info('You number is less than I thought!\n '\
                        if guess < random_number\
                        else 'Your number is greater than I thought!\n')