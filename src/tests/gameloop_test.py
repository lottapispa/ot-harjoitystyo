import unittest
from snake import Snake
from food import Food
from gameloop import GameLoop
from death import Death
from score import Score
from keyboard_events import KeyboardEvents
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

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.gameloop = GameLoop()
        self.screen_size = self.gameloop.screen_size #(640, 480)
        self.snake = Snake(self.screen_size)
        self.food = Food()
        self.score = Score()
        self.death = Death(self.snake, self.score, self.screen_size)
        self.events = KeyboardEvents()
        self.keyboard_events = KeyboardEvents().get()

    def test_correct_screen(self):
        self.assertEqual(self.gameloop.screen_size[0], 640)
        self.assertEqual(self.gameloop.screen_size[1], 480)

    def main_exit(self):
        event = Event(pygame.QUIT)
        get_events = GetEvents(event)
        keyboard = KeyBoard(get_events)
        game_loop = GameLoop()
        snake = Snake(self.screen_size)
        score = Score()
        death = Death(snake, score, self.screen_size)
        snake.dead = True
        death.call_main = False
        death.mouse = (280, 350)
        with self.assertRaises(SystemExit):
            game_loop.main()

    def main_play_again(self):
        event = Event(pygame.MOUSEBUTTONDOWN)
        get_events = GetEvents(event)
        keyboard = KeyBoard(get_events)
        game_loop = GameLoop()
        snake = Snake(self.screen_size)
        score = Score()
        death = Death(snake, score, self.screen_size)
        snake.dead = True
        death.call_main = False
        death.mouse = (280, 310)
        keyboard.keyboard()

        game_loop.main()
        self.assertFalse(death.call_main)

