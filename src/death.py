import sys
import random
import pygame
from keyboard_events import KeyboardEvents
from fonts import Fonts

class Death():
    """Class that handles snake's death."""
    def __init__(self, snake, score):
        """Class constructor, creates variables."""
        self.snake = snake
        self.score = score
        self.fonts = Fonts()
        self.events = KeyboardEvents()
        self.screen_proportions = (640, 480)
        self.screen = None
        self.directions = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        self.die_called = False
        self.call_main = False

    def die(self):
        """Game over window."""
        pygame.init()
        self.die_called = True

        # creating background
        self.screen = pygame.display.set_mode((self.screen_proportions[0], self.screen_proportions[1]))
        self.screen.fill((255, 248, 220))
        pygame.draw.rect(self.screen, (0, 0, 0), (220, 100, 200, 290))

        #getting texts and blitting them
        self.fonts.rendering_text(self.score)
        self.screen.blit(self.fonts.game_over, (250, 130))
        self.screen.blit(self.fonts.points, (275, 175))
        self.screen.blit(self.fonts.time, (275, 215))
        self.screen.blit(self.fonts.highscore, (275, 255))
        self.screen.blit(self.fonts.play_again, (275, 295))
        self.screen.blit(self.fonts.quit_game, (275, 335))

        pygame.display.flip()
        #self.reset()
        while True:
            self.gameover_loop()
            if self.call_main:
                break

    def gameover_loop(self):
        """Game over window's while loop's content.
        Makes buttons in gameover window work."""
        for event in self.events.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 275 <= mouse[0] <= 355 and 295 <= mouse[1] <= 320:
                    self.call_main = True
                    #self.reset()
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 275 <= mouse[0] <= 355 and 335 <= mouse[1] <= 360:
                    sys.exit()

    def reset(self):
        """Resets values for a new game."""
        self.call_main = True
        self.snake.length = 1
        self.snake.location = [((self.screen_proportions[0]/2), (self.screen_proportions[1]/2))]
        self.snake.direction = random.choice(list(self.directions.values()))
        self.score.points = 0
        self.snake.duration = 0
        self.snake.dead = False
        self.die_called = False
