import sys
import pygame

class KeyBoard():
    """Class that has the game's main loop."""
    def __init__(self, snake, screen_size, keyboard_events):
        """Class constructor."""
        self.snake = snake
        self.screen_size = screen_size
        self.events = keyboard_events

    def keyboard(self):
        for event in self.events.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.turn_up()
                if event.key == pygame.K_DOWN:
                    self.snake.turn_down()
                if event.key == pygame.K_LEFT:
                    self.snake.turn_left()
                if event.key == pygame.K_RIGHT:
                    self.snake.turn_right()
            if event.type == pygame.QUIT:
                sys.exit()
