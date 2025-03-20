import re
import sys
import random
import logging
from typing import Callable

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

class Valids:
    def set_valid_values(self, prompt: str, max_length: int, condition: Callable) -> None:
        while True:
            try:
                values = list(map(int, input(prompt).split()))
                if len(values) not in range(1, max_length + 1):
                    logger.error(f"At least one and at most {max_length} values are allowed! Try again!")
                elif condition(values):
                    self.values = values
                    return
                else:
                    logger.error(f"Out of range! Try again!")
            except ValueError:
                logger.error("Invalid input, only integer is allowed! Try again.")

    def get_valid_values(self) -> list:
        return self.values

    def set_valid_number(self, prompt: str, min_value: int, max_value: int) -> None:
        while True:
            try:
                value = int(input(prompt))
                if value in range(min_value, max_value + 1):
                    self.value = value
                    return
                else:
                    logger.error(f"Out of range! Only values between {min_value} and {max_value} are allowed! Try again!")
            except ValueError:
                logger.error("Invalid input! Only integer is allowed! Try again!")

    def get_valid_number(self) -> int:
        return self.value

    def set_valid_string(self, prompt: str, *args) -> None:
        while True:
            value = input(prompt)
            if value in args:
                self.valid_string = value
                return
            else:
                logger.error(f"Invalid input! You can chose only from {args}. Try again!")

    def get_valid_string(self) -> str:
        return self.valid_string

class Menu:
    def __init__(self, game: str) -> None:
        self.valid = Valids()
        self.game = game
        logger.info(f"Entered to the {self.game} game!")
        
    def ask_to_play(self) -> bool:
        self.valid.set_valid_string("Do you want to play the game? (yes/no): ", "yes", "no")
        return self.valid.get_valid_string() == "yes"

class Operations:
    def add_number(self, *args) -> int:
        return sum(args)

    def subtract_number(self, *args) -> int:
        return args[0] - sum(args[1:])

    def multiply_number(self, *args) -> int:
        result = 1
        for i in args:
            result *= i
        return result

    def divide_number(self, *args) -> int:
        result = args[0]
        for i in args[1:]:
            result /= i
        return result

class Equations:
    def is_valid(self, some_equation: str) -> bool:
        pattern = r'^-?0?[0-9]*x2[+-]0?[0-9]*x[+-]0?[0-9]*=0$'
        return bool(re.match(pattern=pattern, string=some_equation))

    def check_equation(self, prompt: str) -> str:
        while True:
            equation = input(prompt)
            if self.is_valid(equation):
                return equation
            else:
                logger.error("Invalid equation! Try again!")

    def get_coefficients(self, equation: str) -> tuple:
        new = equation.split('x')
        a = new[0]
        b = new[1][1:]
        c = new[-1].split('=')[0]
        return a, b, c

    def make_integers(self, a, b, c):
        a = -1 if a == '-' else 1 if a == '' else int(a)
        b = -1 if b == '-' else 1 if b == '' else int(b)
        c = int(c)
        return a, b, c

    def get_discriminant(self, a, b, c):
        return b**2 - 4 * a * c

    def get_solutions(self, a, b, c, discriminant):
        if discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            return x1, x2
        elif discriminant == 0:
            x = -b / (2 * a)
            return x
        else:
            return "No solutions."

class Process:
    def __init__(self) -> None:
        self.operation = Operations()
        self.equation = Equations()
    
    def get_actions(self) -> dict:
        return {'add': self.operation.add_number,
                'subtract': self.operation.subtract_number,
                'multiply': self.operation.multiply_number,
                'divide': self.operation.divide_number,
                'get_coefficients': self.equation.get_coefficients,
                'make_integers': self.equation.make_integers,
                'get_discriminant': self.equation.get_discriminant,
                'get_solutions': self.equation.get_solutions}

class Calculator(Menu):
    def __init__(self) -> None:
        super().__init__(game="Calculator")
        self.process = Process()

    def play(self):
        options = "Choose the operation (add/subtract/multiply/divide): "
        self.valid.set_valid_string(options, "add", "subtract", "multiply", "divide")
        option = self.valid.get_valid_string()
        self.valid.set_valid_values('Enter the max number of values you want to calculate (1-10): ', 1, lambda x: x[0] in range(1, 11))
        length = self.valid.get_valid_values()[0]
        min_value, max_value = 1, 1000
        prompt = f"Enter the values separated by space! Only positive number is allowed from {min_value} to {max_value}: "
        conditions = lambda x: all(i in range(1, 1001) for i in x)
        self.valid.set_valid_values(prompt, length, conditions)
        numbers = self.valid.get_valid_values()
        result = self.process.get_actions()[option](*numbers)
        sign = '+' if option == 'add' else '-' if option == 'subtract' else '*' if option == 'multiply' else '/'
        expression = f"{sign}".join(map(str, numbers))
        logger.info(f"{expression} = {result}")

class GameEquation(Menu):
    def __init__(self):
        super().__init__(game="Quadratic Equation Solver")
        self.process = Process()

    def play(self):
        equation = self.process.equation.check_equation("Enter the equation in the format (-)ax2(+-)bx(+-)c=0: ")
        a, b, c = self.process.get_actions()['get_coefficients'](equation)
        a, b, c = self.process.get_actions()['make_integers'](a, b, c)
        discriminant = self.process.get_actions()['get_discriminant'](a, b, c)
        logger.info(f"The solutions are: {self.process.get_actions()['get_solutions'](a, b, c, discriminant)}\n")

class ChickenRabbit(Menu):
    def __init__(self):
        super().__init__(game="Chicken and Rabbit")

    def set_params(self):
        MIN_VALUE, MAX_VALUE = 1, 100
        heads_string = f"Enter the number of heads from {MIN_VALUE} - {MAX_VALUE}: "
        self.valid.set_valid_number(heads_string, MIN_VALUE, MAX_VALUE)
        self.number_of_heads = self.valid.get_valid_number()
        legs_string = f"Enter the number of legs from {self.number_of_heads*2} - {self.number_of_heads*4}: "
        self.valid.set_valid_number(legs_string, self.number_of_heads*2, self.number_of_heads * 4)
        self.number_of_legs = self.valid.get_valid_number()
    
    def get_params(self) -> tuple:
        return self.number_of_heads, self.number_of_legs

    def play(self):
        self.set_params()
        number_of_heads, number_of_legs = self.get_params()
        
        found_soulutions = False
        for num_chicken in range(number_of_heads + 1):
            num_rabbit = number_of_heads - num_chicken
            if num_chicken * 2 + num_rabbit * 4 == number_of_legs:
                logger.info(f"Number of chickens: {num_chicken}, Number of rabbits: {num_rabbit}")
                found_soulutions = True
        if not found_soulutions:
            logger.info("No solutions found!")

class Guesses(Menu):
    def __init__(self):
        super().__init__(game="Guess the Number")

    def play(self) -> None:
        random_number, count = random.randint(1, 100), 0
        logger.info('I thought of a number from 1 to 100! Find out what is it! ')
        while True:
            count += 1
            self.valid.set_valid_number(f'Enter your No. {count} guess! ', 1, 100)
            guess = self.valid.get_valid_number()
            if guess == random_number: 
                logger.info(f'You just hit, won. ')
                return
            logger.info('You number is less than I thought!\n ' if guess < random_number else 'Your number is greater than I thought!\n')

class Lotto(Menu):
    def __init__(self):
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
        logger.info('CONGRATULATIONS! YOU WON THE LOTTERY! ' if good_nums == len(winning_nums) else f'You have {good_nums} match(es).')
        
class Rock(Menu):
    def __init__(self):
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
            if (result[0] == 'rock' and result[1] not in ['rock', 'paper'])
            or (result[0] == 'paper' and result[1] not in ['paper', 'scissors'])
            or result[0] == 'scissors' and result[1] not in ['scissors', 'rock']
            else f'Even! Computer chose {computer}. ' if result[0] == result[1]
            else f'You lost, Computer chose {computer}.')

class Games(Menu):
    def __init__(self) -> None:
        self.valid = Valids()
        self.games = dict(enumerate([Calculator, GameEquation, ChickenRabbit, Guesses, Lotto, Rock], 1))
        self.games[len(self.games) + 1] = sys.exit

    def set_game(self):
        games_options = ''
        for game_number  in self.games:
            games_options += f"{game_number}. {self.games[game_number].__name__}\n"
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

if __name__ == '__main__':
    logger.info("Welcome to the Game Center!\n")
    games = Games()
    while True:
        games.set_game()
        if games.get_game() == len(games.games):
            logger.info("Thank you for playing! Goodbye!")
            break
        games.play_game()