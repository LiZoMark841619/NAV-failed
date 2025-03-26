from menu import Menu
from logsettings import logger
from process import Process

class Calculator(Menu):
    def __init__(self) -> None:
        super().__init__(game="Calculator")
        self.process = Process()

    def play(self) -> None:
        options = "Choose the operation (add/subtract/multiply/divide): "
        self.valid.set_valid_string(options, "add", "subtract", "multiply", "divide")
        option = self.valid.get_valid_string()
        min_value, max_value = 1, 1000
        prompt = f"Enter the values separated by space! Only positive number is allowed from {min_value} to {max_value}: "
        conditions = lambda x: all(i in range(1, 1001) for i in x)
        self.valid.set_valid_values(prompt, conditions)
        numbers = self.valid.get_valid_values()
        result = self.process.get_actions()[option](*numbers)
        sign = '+' if option == 'add' else '-' if option == 'subtract' else '*' if option == 'multiply' else '/'
        expression = f"{sign}".join(map(str, numbers))
        logger.info(f"{expression} = {result}")