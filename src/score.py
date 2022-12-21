import pygame

class Score():
    """Class that keeps track of score."""
    def __init__(self):
        """Class constructor, creates variables."""
        self.points = 0
        self.highscore = 0

    def eating(self, snake, food):
        """Grows snake and adds points if snake eats food."""
        if pygame.Rect.collidepoint(snake.head_rect(), food.location) is True:
            snake.length += 1
            self.points += 1
            if self.points > self.highscore:
                self.highscore = self.points
            food.random_location()
