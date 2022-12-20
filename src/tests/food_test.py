import unittest
from snake import Snake
from food import Food
from keyboard_events import KeyboardEvents
import pygame

class TestFood(unittest.TestCase):
    def setUp(self):
        food = Food()
        self.size = food.size
        self.color = food.color
        self.location = food.location
        snake = Snake()
        self.length = snake.length
        self.points = snake.points
        self.highscore = snake.highscore

    def test_correct_size(self):
        self.assertEqual(self.size, 10)

    def test_correct_color(self):
        self.assertEqual(self.color, (139,69,19))

    def test_correct_random_location(self):
        #checks location is not out of bounds
        self.assertGreater(self.location[0], 9)
        self.assertGreater(self.location[1], 9)
        self.assertLess(self.location[0], 631)
        self.assertLess(self.location[1], 471)

    def draw_food(self):
        pass

    def test_eating(self):
        food = Food()
        food.location = (40, 40)
        snake = Snake()
        snake.location = [(40, 40)]
        food.eating(snake)
        self.assertEqual(snake.length, 2)
        self.assertEqual(snake.points, 1)
        