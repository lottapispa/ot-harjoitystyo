import sys
import random
import pygame
from keyboard_events import KeyboardEvents
from fonts import Fonts

class Death():
    """Class that handles snake's death."""
    def __init__(self, snake, score, screen_size):
        """Class constructor, creates variables."""
        self.snake = snake
        self.score = score
        self.fonts = Fonts()
        self.events = KeyboardEvents()
        self.screen_size = screen_size
        self.screen = None
        self.directions = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        self.mouse = pygame.mouse.get_pos()
        self.die_called = False
        self.call_main = False

    def die(self):
        """Game over window."""
        pygame.init()
        self.die_called = True

        # creating background
        self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.screen.fill((255, 248, 220))
        pygame.draw.rect(self.screen, (0, 0, 0), (220, 100, 200, 250))
        pygame.draw.rect(self.screen, (50, 50, 50), (270, 250, 95, 25))
        pygame.draw.rect(self.screen, (50, 50, 50), (270, 290, 95, 25))

        #getting texts and blitting them
        self.fonts.rendering_text(self.score)
        self.screen.blit(self.fonts.game_over, (250, 130))
        self.screen.blit(self.fonts.points, (275, 175))
        self.screen.blit(self.fonts.highscore, (275, 215))
        self.screen.blit(self.fonts.play_again, (275, 255))
        self.screen.blit(self.fonts.quit_game, (275, 295))

        pygame.display.flip()

    def gameover_loop(self):
        """Game over window's while loop's content.
        Makes buttons in gameover window work."""
        for event in self.events.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse = pygame.mouse.get_pos()
                if 270 <= self.mouse[0] <= 365 and 250 <= self.mouse[1] <= 275:
                    self.call_main = True
                elif 270 <= self.mouse[0] <= 365 and 290 <= self.mouse[1] <= 315:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

    def reset(self):
        """Resets values for a new game."""
        self.snake.length = 1
        self.snake.location = [((self.screen_size[0]/2), (self.screen_size[1]/2))]
        self.snake.direction = random.choice(list(self.directions.values()))
        self.score.points = 0
        self.snake.dead = False
        self.die_called = False
        self.call_main = False
