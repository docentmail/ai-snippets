## utils.py
import os
import random

class Utils:
    @staticmethod
    def clear_screen():
        """
        Clears the console screen.
        """
        # Check if the operating system is Windows
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def generate_food(snake, board_width=20, board_height=20):
        """
        Generates a new food position that is not occupied by the snake.

        Args:
            snake (list): The current positions of the snake segments.
            board_width (int, optional): The width of the game board. Defaults to 20.
            board_height (int, optional): The height of the game board. Defaults to 20.

        Returns:
            tuple: The position (x, y) of the new food.
        """
        while True:
            food = (random.randint(1, board_width-1), random.randint(1, board_height-1))
            if food not in snake:
                return food
