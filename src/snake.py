import random
import sys
import pygame

class Snake():
    """Class that creates and keeps track of snake."""
    def __init__(self):
        """Class constructor, creates variables."""
        pygame.init()
        self.length = 1
        self.color = (102, 205, 0)
        self.screen_width = 640
        self.screen_height = 480
        self.location = [((self.screen_width/2), (self.screen_height/2))]
        self.up = (0, -1)
        self.down = (0, 1)
        self.left = (-1, 0)
        self.right = (1, 0)
        self.direction = random.choice([self.up,self.down,self.left,self.right])
        self.points = 0
        self.highscore = 0
        self.step = 20 # how much snake moves at once
        self.duration = 0 # tracks how long the game lasts (not used yet)
        self.die_called = False
        self.reset_called = False
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
            if self.counter == 0:
                pygame.draw.rect(screen, self.color, pygame.Rect((location[0], location[1]), (20, 20)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((location[0], location[1]), (20, 20)), 1)
            else:
                pygame.draw.rect(screen, self.color, pygame.Rect((location[0], location[1]), (20, 20)))
            self.counter += 1

    """These functions are called by the keyboard function and they change the direction variable."""
    def turn_up(self):
        if self.direction != self.down or self.direction != self.up or self.length == 1:
            self.direction = self.up

    def turn_down(self):
        if self.direction != self.up or self.direction != self.down or self.length == 1:
            self.direction = self.down

    def turn_left(self):
        if self.direction != self.right or self.direction != self.left or self.length == 1:
            self.direction = self.left

    def turn_right(self):
        if self.direction != self.left or self.direction != self.right or self.length == 1:
            self.direction = self.right

    def move(self):
        """Moves snake by adding a new location in list and popping the last location."""
        self.current = self.head_location()
        x = self.direction[0]
        y = self.direction[1]
        if self.direction == self.up or self.direction == self.down:
            self.new_head = (self.current[0], self.current[1] + (self.step * y))
        elif self.direction == self.left or self.direction == self.right:
            self.new_head = (self.current[0] + (self.step * x), self.current[1])
        # snake dies if it hits itself or a wall
        if len(self.location) > 2 and self.new_head in self.location[2:]:
            self.dead = True
        elif self.new_head[0] + 20 > 640 or self.new_head[0] < 0 or self.new_head[1] + 20 > 480 or self.new_head[1] < 0:
            self.dead = True
        else:
            self.location.insert(0, self.new_head)
            if len(self.location) > self.length:
                self.location.pop()

    def reset(self):
        """Resets values for a new game."""
        self.reset_called = True
        self.length = 1
        self.location = [((self.screen_width/2), (self.screen_height/2))] 
        self.direction = random.choice([self.up, self.down, self.left, self.right])
        self.points = 0
        self.duration = 0
        self.dead = False