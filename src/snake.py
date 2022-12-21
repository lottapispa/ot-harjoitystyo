import random
import pygame

class Snake():
    """Class that creates and keeps track of snake."""
    def __init__(self):
        """Class constructor, creates variables."""
        pygame.init()
        self.length = 1
        self.color = (102, 205, 0)
        self.screen_proportions = (640, 480)
        self.location = [((self.screen_proportions[0]/2), (self.screen_proportions[1]/2))]
        self.directions = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        self.direction = random.choice(list(self.directions.values()))
        self.step = 20 # how much snake moves at once
        self.duration = 0 # tracks how long the game lasts (not used yet)
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
        Snake head has a black outline."""
        self.counter = 0
        for location in self.location:
            self.rect = pygame.Rect((location[0], location[1]), (20, 20))
            if self.counter == 0:
                pygame.draw.rect(screen, self.color, self.rect)
                pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
            else:
                pygame.draw.rect(screen, self.color, self.rect)
            self.counter += 1

    def turn_up(self):
        """These turn functions are called by the keyboard function.
        They change the direction variable."""
        if self.direction not in (self.directions["down"], self.directions["up"]) or self.length == 1:
            self.direction = self.directions["up"]

    def turn_down(self):
        if self.direction not in (self.directions["up"], self.directions["down"]) or self.length == 1:
            self.direction = self.directions["down"]

    def turn_left(self):
        if self.direction not in (self.directions["right"], self.directions["left"]) or self.length == 1:
            self.direction = self.directions["left"]

    def turn_right(self):
        if self.direction not in (self.directions["left"], self.directions["right"]) or self.length == 1:
            self.direction = self.directions["right"]

    def move(self):
        """Moves snake by adding a new location in list and popping the last location."""
        self.current = self.head_location()
        self.width = self.direction[0]
        self.height = self.direction[1]
        if self.direction in (self.directions["up"], self.directions["down"]):
            self.new_head = (self.current[0], self.current[1] + (self.step * self.height))
        elif self.direction in (self.directions["left"],  self.directions["right"]):
            self.new_head = (self.current[0] + (self.step * self.width), self.current[1])
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
