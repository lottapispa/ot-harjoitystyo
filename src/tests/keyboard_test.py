import unittest
from snake import Snake
from food import Food
from gameloop import GameLoop
from death import Death
from score import Score
from keyboard import KeyBoard
import pygame

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

class TestKeyBoard(unittest.TestCase):
    def setUp(self):
        self.gameloop = GameLoop()
        self.screen_size = self.gameloop.screen_size #(640, 480)
        self.snake = Snake(self.screen_size)
        self.food = Food()
        self.score = Score()
        self.death = Death(self.snake, self.score, self.screen_size)

    def keyboard_quit(self):
        event = Event(pygame.QUIT)
        get_events = GetEvents(event)
        keyboard = KeyBoard(get_events)
        #snake = Snake(self.screen_size)
        with self.assertRaises(SystemExit):
            keyboard.keyboard()

    def keyboard_press_up(self):
        event = Event(pygame.KEYDOWN,pygame.K_UP)
        get_events = GetEvents(event)
        keyboard = KeyBoard(get_events)
        snake = Snake(self.screen_size)
        snake.direction = snake.directions["left"]
        snake.length == 2
        keyboard.keyboard()
        self.assertEqual(snake.direction, (0, -1))
