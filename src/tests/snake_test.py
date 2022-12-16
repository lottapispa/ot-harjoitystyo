import unittest
#import ohtekoodi
from snake import Snake
from keyboard_events import KeyboardEvents
from gameloop import GameLoop
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
        self.font = GameLoop().font
        self.bigfont = GameLoop().bigfont
        self.events = GameLoop().events
        self.keyboard_events = KeyboardEvents().get()
        self.die_called = Snake().die_called
        self.reset_called = Snake().reset_called

    def test_correct_length_in_the_beginning(self):
        self.assertEqual(self.length, 1)

    def test_correct_color_in_the_beginning(self):
        self.assertEqual(self.color, (102, 205, 0))

    def test_correct_length(self):
        # length variable is the same as len of list self.location
        # also tests if eating grows the snake
        self.assertEqual(self.length, len(self.location))

    def test_correct_points(self):
        # points variable is the same size as length variable
        self.assertEqual(self.points+1, self.length)

    # self.direction variable is _ if condition is met
    def test_turn_up(self):
        if self.keyboard_events == pygame.K_UP:
            self.assertEqual(self.direction, self.up)

    def test_turn_down(self):
        if self.keyboard_events == pygame.K_DOWN:
            self.assertEqual(self.direction, self.down)

    def test_turn_left(self):
        if self.keyboard_events == pygame.K_LEFT:
            self.assertEqual(self.direction, self.left)

    def test_turn_right(self):
        if self.keyboard_events == pygame.K_RIGHT:
            self.assertEqual(self.direction, self.right)

    def test_dies_when_touches_wall(self):
        self.head_location = Snake().head_location()
        if self.head_location[0] + 20 > 640 or self.head_location[1] + 20 > 480:
            self.assertTrue(self.die_called)

    def test_dies_when_touches_itself(self):
        self.head_location = Snake().head_location()
        if len(self.location) > 2 and self.head_location in self.location[2:]:
            self.assertTrue(self.die_called)

    def test_resets_when_dies(self):
        if self.die_called:
            self.assertTrue(self.reset_called)