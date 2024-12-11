## game.py
import keyboard
import time
from utils import Utils

class Game:
    def __init__(self):
        self.score = 0
        self.snake = [(10, 10), (10, 11), (10, 12)]
        self.food = None
        self.is_game_over = False
        self.board_width = 20
        self.board_height = 20
        self.direction = 'UP'

    def start_game(self):
        """
        Initializes the game by generating the first food and setting up the initial game state.
        """
        self.food = Utils.generate_food(self.snake, self.board_width, self.board_height)
        self.is_game_over = False
        self.score = 0
        self.main_loop()

    def process_input(self):
        """
        Processes keyboard input and updates the snake's direction accordingly.
        """
        if keyboard.is_pressed('up') and self.direction != 'DOWN':
            self.direction = 'UP'
        elif keyboard.is_pressed('down') and self.direction != 'UP':
            self.direction = 'DOWN'
        elif keyboard.is_pressed('left') and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif keyboard.is_pressed('right') and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def update_game_state(self):
        """
        Updates the game state, including moving the snake and checking for collisions.
        """
        head_x, head_y = self.snake[0]

        if self.direction == 'UP':
            head_y -= 1
        elif self.direction == 'DOWN':
            head_y += 1
        elif self.direction == 'LEFT':
            head_x -= 1
        elif self.direction == 'RIGHT':
            head_x += 1

        new_head = (head_x, head_y)

        # Check for collisions with walls
        if head_x < 0 or head_x >= self.board_width or head_y < 0 or head_y >= self.board_height:
            self.is_game_over = True
            return

        # Check for collisions with itself
        if new_head in self.snake:
            self.is_game_over = True
            return

        self.snake.insert(0, new_head)

        # Check if food is eaten
        if new_head == self.food:
            self.score += 1
            self.food = Utils.generate_food(self.snake, self.board_width, self.board_height)
        else:
            self.snake.pop()

    def render(self):
        """
        Renders the game state to the console.
        """
        Utils.clear_screen()
        print(f"Score: {self.score}")
        for y in range(self.board_height):
            for x in range(self.board_width):
                if (x, y) == self.snake[0]:
                    print("H", end='')
                elif (x, y) in self.snake:
                    print("S", end='')
                elif (x, y) == self.food:
                    print("F", end='')
                else:
                    print(".", end='')
            print()

    def main_loop(self):
        """
        The main game loop, processing input, updating the game state, and rendering until the game is over.
        """
        while not self.is_game_over:
            self.process_input()
            self.update_game_state()
            self.render()
            time.sleep(0.1)  # Correct method to slow down the game loop

        print("Game Over! Your final score is:", self.score)
