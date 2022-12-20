import random
import pygame

class Food():
    """Class that creates and keeps track of food"""
    def __init__(self):
        """Class constructor, creates variables."""
        self.size = 10 # radius
        self.color = (139,69,19)
        self.location = (0,0) # center point of circle
        self.random_location()

    def random_location(self):
        """Assigns random location for food to pop up in."""
        self.location = (random.randint(10, 640-10), random.randint(10, 480-10))

    def draw_food(self, screen):
        """Draws food."""
        pygame.draw.circle(screen, self.color, self.location, self.size)

    def eating(self, snake):
        """Grows snake and adds points if snake eats food."""
        if pygame.Rect.collidepoint(snake.head_rect(), self.location) is True:
            snake.length += 1
            snake.points += 1
            if snake.points > snake.highscore:
                snake.highscore = snake.points
            self.random_location()
