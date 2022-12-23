import unittest
from snake import Snake
from death import Death
from score import Score
from gameloop import GameLoop
from keyboard_events import KeyboardEvents
import pygame

class TestDeath(unittest.TestCase):
    def setUp(self):
        self.game_loop = GameLoop()
        self.screen_size = self.game_loop.screen_size #(640, 480)
        self.snake = Snake(self.screen_size)
        self.score = Score()
        self.death = Death(self.snake, self.score, self.screen_size)
        self.die_called = self.death.die_called

    def test_die_called_boolean_correct(self):
        self.death.die_called = False
        self.death.die()
        self.assertTrue(self.death.die_called)

    def test_correct_screen(self):
        self.assertEqual(self.screen_size[0], 640)
        self.assertEqual(self.screen_size[1], 480)

    def test_reset_works_correctly(self):
        self.death.reset()
        self.assertEqual(self.snake.length, 1)
        self.assertEqual(self.snake.location, [((self.snake.screen_size[0]/2), (self.snake.screen_size[1]/2))])
        self.assertEqual(self.score.points, 0)
        self.assertEqual(self.score.highscore, 0)
        self.assertEqual(self.snake.duration, 0)
        self.assertFalse(self.snake.dead)
        self.assertFalse(self.death.die_called)
        self.assertFalse(self.death.call_main)

    def gameover_loop_does_button_play_again_work(self):
        #?
        snake = Snake(self.screen_size)
        score = Score()
        death = Death(snake, score, self.screen_size)
        death.call_main = False
        death.mouse = (280, 310)
        death.event.type = pygame.MOUSEBUTTONDOWN
        death.gameover_loop()
        self.assertTrue(death.call_main)

    def gameover_loop_does_button_quit_work(self):
        #?
        snake = Snake(self.screen_size)
        score = Score()
        death = Death(snake, score, self.screen_size)
        death.call_main = False
        death.mouse = (280, 350)
        death.event.type = pygame.MOUSEBUTTONDOWN
        with self.assertRaises(SystemExit):
            death.gameover_loop()

