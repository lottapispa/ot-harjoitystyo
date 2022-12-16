import random
import sys
import pygame
from ohtekoodi import Snake
from ohtekoodi import Food

class GameLoop():
    """Class that has the game's main loop."""
    def __init__(self):
        """Class constructor, creates variables, calls other classes."""
        self.snake = Snake()
        self.food = Food()
        self.screen_width = 640
        self.screen_height = 480
        pygame.display.set_caption("Snake")

    def main(self):
        """Main loop."""
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        clock = pygame.time.Clock()
        
        while True:
            self.snake.keyboard()
            screen.fill((255, 248, 220)) 
            self.snake.move()
            self.snake.draw_snake(screen)
            self.food.draw_food(screen)
            self.food.eating(self.snake)
            pygame.display.flip()
            clock.tick(10)

if __name__ == "__main__":
    GameLoop().main()