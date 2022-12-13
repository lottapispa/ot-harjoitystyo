import unittest
#import ohtekoodi
from ohtekoodi import Snake
from ohtekoodi import Food
import random
import sys
import pygame


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.length = Snake().length
        self.color = Snake().color
        self.up = Snake().up
        self.down = Snake().down
        self.left = Snake().left
        self.right = Snake().right
        self.location = Snake().location
        self.direction = Snake().direction
        self.points = Snake().points
        self.font = Snake().font
        self.bigfont = Snake().bigfont
        self.events = Snake().events
        self.events = Snake().events

    def test_correct_length_in_the_beginning(self):
        self.assertEqual(self.length, 1)

    def test_correct_color_in_the_beginning(self):
        self.assertEqual(self.color, (102, 205, 0))

    def test_correct_length(self):
        # length variable is the same as len of list self.location
        self.assertEqual(self.length, len(self.location))

    def test_correct_points(self):
        # points variable is the same size as length variable
        self.assertEqual(self.points+1, self.length)

    # self.direction variable is _ if condition is met
    def test_turn_up(self):
        if self.event.key == pygame.K_UP:
            self.assertEqual(self.direction, self.up)

    def test_turn_down(self):
        if self.event.key == pygame.K_DOWN:
            self.assertEqual(self.direction, self.down)

    def test_turn_left(self):
        if self.event.key == pygame.K_LEFT:
            self.assertEqual(self.direction, self.left)

    def test_turn_right(self):
        if self.event.key == pygame.K_RIGHT:
            self.assertEqual(self.direction, self.right)

    def dies_when_touches_wall(self):
        pass

    def dies_when_touches_itself(self):
        pass

    def test_resets_when_dies(self):
        self.die_called = Snake().die_called
        self.reset_called = Snake().reset_called
        if self.die_called:
            self.assertTrue(self.reset_called)

    def eating(self):
        pass

    def die(self):
        pass
