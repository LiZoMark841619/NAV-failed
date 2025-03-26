from typing import Callable
from logsettings import logger

class Valids:
    def set_valid_values(self, prompt: str, condition: Callable) -> None:
        while True:
            try:
                values = list(map(int, input(prompt).split()))
                if condition(values):
                    self.values = values
                    return
                else:
                    logger.error("Out of range! Try again!")
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