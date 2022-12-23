import unittest
from snake import Snake
from food import Food
from gameloop import GameLoop
from death import Death
from score import Score
from keyboard_events import KeyboardEvents

#classes for testing keyboard and mouse presses
class Event():
    def __init__(self, event_type):
        self.type = event_type

class Events():
    def __init__(self, event_type, event_key):
        self.type = event_type
        self.key = event_key

class GetEvents():
    def __init__(self, events):
        self.events = events

    def get(self):
        return self.events

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.gameloop = GameLoop()
        self.screen_size = self.gameloop.screen_size
        self.snake = Snake(self.screen_size)
        self.food = Food()
        self.score = Score()
        self.death = Death(self.snake, self.score, self.screen_size)
        self.events = KeyboardEvents()
        self.keyboard_events = KeyboardEvents().get()

    def test_correct_screen(self):
        self.assertEqual(self.gameloop.screen_size[0], 640)
        self.assertEqual(self.gameloop.screen_size[1], 480)
