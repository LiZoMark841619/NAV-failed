from logsettings import logger
from process import Process
from menu import Menu

class GameEquation(Menu):
    def __init__(self) -> None:
        super().__init__(game="Quadratic Equation Solver")
        self.process = Process()

    def play(self):
        equation = self.process.equation.check_equation("Enter the equation in the format (-)ax2(+-)bx(+-)c=0: ")
        a, b, c = self.process.get_actions()['get_coefficients'](equation)
        a, b, c = self.process.get_actions()['make_integers'](a, b, c)
        discriminant = self.process.get_actions()['get_discriminant'](a, b, c)
        logger.info(f"The solutions are: {self.process.get_actions()['get_solutions'](a, b, c, discriminant)}\n")