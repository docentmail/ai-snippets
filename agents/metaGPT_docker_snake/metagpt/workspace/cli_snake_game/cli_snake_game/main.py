## main.py
from game import Game

class Main:
    @staticmethod
    def main():
        """
        The entry point of the application. It creates an instance of the Game class and starts the game.
        """
        game_instance = Game()
        game_instance.start_game()

if __name__ == "__main__":
    Main.main()
