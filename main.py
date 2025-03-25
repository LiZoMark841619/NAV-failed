from logsettings import logger
from games import Games

if __name__ == '__main__':
    logger.info("Welcome to the Game Center!\n")
    games = Games()
    while True:
        games.set_game()
        if games.get_game() == len(games.games):
            logger.info("Thank you for playing! Goodbye!")
            break
        games.play_game()
