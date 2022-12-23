import pygame

class KeyboardEvents():
    """Class that is for dependency injection."""
    def get(self):
        return pygame.event.get()
