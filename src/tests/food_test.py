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

    def eating(self, snake):
        pass