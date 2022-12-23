import pygame

class Fonts():
    """Class that handles fonts and text."""
    def __init__(self):
        """Class constructor, creates variables."""
        self.font = pygame.font.SysFont("Candara", 24)
        self.bigfont = pygame.font.SysFont("Candara", 36)
        self.game_over = None
        self.points = None
        self.highscore = None
        self.play_again = None
        self.quit_game = None

    def rendering_text(self, score):
        """Makes texts for game over window."""
        self.game_over = self.bigfont.render("Game Over", True, (255, 97, 3))
        self.points = self.font.render(f"Points: {score.points}", True, (255, 248, 220))
        self.highscore = self.font.render(f"Highscore: {score.highscore}", True, (255, 248, 220))
        self.play_again = self.font.render("Play Again", True, (255, 248, 220))
        self.quit_game = self.font.render("Quit Game", True, (255, 248, 220))
