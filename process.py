from logsettings import logger
import re

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

    def make_integers(self, a, b, c) -> tuple:
        a = -1 if a == '-' else 1 if a == '' else int(a)
        b = -1 if b == '-' else 1 if b == '' else int(b)
        c = int(c)
        return a, b, c

    def get_discriminant(self, a, b, c) -> int:
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