import sys
import random
import pygame
from keyboard_events import KeyboardEvents

class Death():
    """Class that """
    def __init__(self, snake, score):
        """Class constructor, creates variables."""
        self.snake = snake
        self.score = score
        self.events = KeyboardEvents()
        self.screen_proportions = (640, 480)
        self.font = pygame.font.SysFont("Candara", 24)
        self.bigfont = pygame.font.SysFont("Candara", 36)
        self.directions = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        self.die_called = False
        self.reset_called = False
        self.call_main = False

    def die(self):
        """Game over window."""
        pygame.init()
        self.die_called = True
        screen = pygame.display.set_mode((self.screen_proportions[0], self.screen_proportions[1]))
        screen.fill((255, 248, 220))
        pygame.draw.rect(screen, (0, 0, 0), (220, 100, 200, 290))

        #texts and blitting them
        game_over = self.bigfont.render("Game Over", True, (255, 97, 3))
        screen.blit(game_over, (250, 130))

        points = self.font.render(f"Points: {self.score.points}", True, (255, 248, 220))
        screen.blit(points, (275, 175))

        time = self.font.render("Time: ", True, (255, 248, 220))
        screen.blit(time, (275, 215))

        highscore = self.font.render(f"Highscore: {self.score.highscore}", True, (255, 248, 220))
        screen.blit(highscore, (275, 255))

        play_again = self.font.render("Play Again", True, (255, 248, 220))
        screen.blit(play_again, (275, 295))

        quit_game = self.font.render("Quit Game", True, (255, 248, 220))
        screen.blit(quit_game, (275, 335))

        pygame.display.flip()
        while True:
            self.gameover_loop()

    def gameover_loop(self):
        """Game over window's while loop's content.
        Makes buttons in gameover window work."""
        for event in self.events.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 275 <= mouse[0] <= 355 and 295 <= mouse[1] <= 320:
                    self.reset()
                    self.call_main = True
                    self.reset_called  = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 275 <= mouse[0] <= 355 and 335 <= mouse[1] <= 360:
                    sys.exit()

    def reset(self):
        """Resets values for a new game."""
        self.reset_called = True
        self.snake.length = 1
        self.snake.location = [((self.screen_proportions[0]/2), (self.screen_proportions[1]/2))]
        self.snake.direction = random.choice(list(self.directions.values()))
        self.score.points = 0
        self.snake.duration = 0
        self.snake.dead = False
        self.die_called = False
