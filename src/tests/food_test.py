import unittest
from snake import Snake
from food import Food
from keyboard_events import KeyboardEvents
import random
import sys
import pygame

class TestFood(unittest.TestCase):
    def setUp(self):
        self.size = Food().size
        self.color = Food().color
        self.location = Food().location
        self.length = Snake().length
        self.points = Snake().points
        self.highscore = Snake().highscore

    def test_correct_size(self):
        self.assertEqual(self.size, 10)

    def test_correct_color(self):
        self.assertEqual(self.color, (139,69,19))

    def test_correct_location(self):
        #checks location is not out of bounds
        self.assertGreater(self.location[0], 9)
        self.assertGreater(self.location[1], 9)
        self.assertLess(self.location[0], 631)
        self.assertLess(self.location[1], 471)

    def test_eating(self):
        food = Food()
        food.location = (40, 40)
        snake = Snake()
        snake.location = [(40, 40)]
        food.eating(snake)
        self.assertEqual(snake.length, 2)
        self.assertEqual(snake.points, 1)
        