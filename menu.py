from logsettings import logger
from valids import Valids

class Menu:
    def __init__(self, game: str) -> None:
        self.valid = Valids()
        self.game = game
        logger.info(f"Entered to the {self.game} game!")
        
    def ask_to_play(self) -> bool:
        self.valid.set_valid_string("Do you want to play the game? (yes/no): ", "yes", "no")
        return self.valid.get_valid_string() == "yes"