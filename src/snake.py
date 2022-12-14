import random
import pygame

class Snake():
    """Class that creates and keeps track of snake."""
    def __init__(self, screen_size):
        """Class constructor, creates variables."""
        pygame.init()
        self.length = 1
        self.color = (102, 205, 0)
        self.screen_size = screen_size
        self.location = [((self.screen_size[0]/2), (self.screen_size[1]/2))]
        self.directions = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        self.direction = random.choice(list(self.directions.values()))
        self.counter = 0
        self.step = 20 # how much snake moves at once
        self.dead = False

    def head_location(self):
        """Returns: location of snake's head"""
        return self.location[0]

    def head_rect(self):
        """Returns: snake's head rectangle"""
        self.head = self.location[0]
        self.rect = pygame.Rect((self.head[0], self.head[1]), (20, 20))
        return self.rect

    def draw_snake(self, screen):
        """Draws snake  by drawing a rectangle in every location in list.
        Snake's head has a black outline."""
        self.counter = 0
        for loc in self.location:
            self.rect = pygame.Rect((loc[0], loc[1]), (20, 20))
            if self.counter == 0:
                pygame.draw.rect(screen, self.color, self.rect)
                pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
            else:
                pygame.draw.rect(screen, self.color, self.rect)
            self.counter += 1

    def turn_up(self):
        """These turn functions are called by the keyboard function.
        They change the direction variable."""
        if self.direction in (self.directions["left"],self.directions["right"]) or self.length == 1:
            self.direction = self.directions["up"]

    def turn_down(self):
        if self.direction in (self.directions["left"],self.directions["right"]) or self.length == 1:
            self.direction = self.directions["down"]

    def turn_left(self):
        if self.direction in (self.directions["up"],self.directions["down"]) or self.length == 1:
            self.direction = self.directions["left"]

    def turn_right(self):
        if self.direction in (self.directions["up"],self.directions["down"]) or self.length == 1:
            self.direction = self.directions["right"]

    def move(self):
        """Moves snake by adding a new location in list and popping the last location."""
        self.current = self.head_location()
        if self.direction in (self.directions["up"], self.directions["down"]):
            self.new_head = (self.current[0], self.current[1] + (self.step * self.direction[1]))
        else:
            self.new_head = (self.current[0] + (self.step * self.direction[0]), self.current[1])
        # snake dies if it hits itself or a wall
        if len(self.location) > 2 and self.new_head in self.location[2:]:
            self.dead = True
        elif self.new_head[0] + 20 > 640 or self.new_head[0] < 0:
            self.dead = True
        elif self.new_head[1] + 20 > 480 or self.new_head[1] < 0:
            self.dead = True
        else:
            self.location.insert(0, self.new_head)
            if len(self.location) > self.length:
                self.location.pop()
