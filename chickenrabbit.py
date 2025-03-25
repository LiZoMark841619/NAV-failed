from menu import Menu
from logsettings import logger

class ChickenRabbit(Menu):
    def __init__(self) -> None:
        super().__init__(game="Chicken and Rabbit")

    def set_params(self) -> None:
        MIN_VALUE, MAX_VALUE = 1, 100
        heads_string = f"Enter the number of heads from {MIN_VALUE} - {MAX_VALUE}: "
        self.valid.set_valid_number(heads_string, MIN_VALUE, MAX_VALUE)
        self.number_of_heads = self.valid.get_valid_number()
        legs_string = f"Enter the number of legs from {self.number_of_heads*2} - {self.number_of_heads*4}: "
        self.valid.set_valid_number(legs_string, self.number_of_heads*2, self.number_of_heads * 4)
        self.number_of_legs = self.valid.get_valid_number()
    
    def get_params(self) -> tuple:
        return self.number_of_heads, self.number_of_legs

    def play(self) -> None:
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