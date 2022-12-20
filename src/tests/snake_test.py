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
        snake = Snake()
        self.length = snake.length
        self.color = snake.color
        self.up = snake.up
        self.down = snake.down
        self.left = snake.left
        self.right = snake.right
        self.location = snake.location
        self.direction = snake.direction
        self.points = snake.points
        self.highscore = snake.highscore
        self.events = GameLoop().events
        self.keyboard_events = KeyboardEvents().get()
        self.die_called = snake.die_called
        self.reset_called = snake.reset_called
        self.dead = snake.dead
        self.head_location = snake.head_location()

    def test_correct_length_in_the_beginning(self):
        self.assertEqual(self.length, 1)

    def test_correct_color_in_the_beginning(self):
        self.assertEqual(self.color, (102, 205, 0))

    def test_correct_points_in_the_beginning(self):
        # points variable is the same size as length variable
        self.assertEqual(self.points, 0)

    def test_correct_highscore_in_the_beginning(self):
        # points variable is the same size as length variable
        self.assertEqual(self.highscore, 0)

    def test_head_location(self):
        self.snake = Snake()
        self.assertEqual(self.snake.head_location(), self.location[0])

    def test_booleans_correct_in_the_beginning(self):
        self.assertFalse(self.die_called)
        self.assertFalse(self.reset_called)
        self.assertFalse(self.dead)

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
        if self.head_location[0] + 20 > 640 or self.head_location[1] + 20 > 480:
            self.assertTrue(self.die_called)

    def test_dies_when_touches_itself(self):
        if len(self.location) > 2 and self.head_location in self.location[2:]:
            self.assertTrue(self.die_called)

    def test_resets_when_dies(self):
        if self.die_called:
            self.assertTrue(self.reset_called)
