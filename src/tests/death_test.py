import unittest
from snake import Snake
from death import Death
from score import Score
from gameloop import GameLoop
import pygame

class TestDeath(unittest.TestCase):
    def setUp(self):
        self.game_loop = GameLoop()
        self.screen_size = self.game_loop.screen_size #(640, 480)
        self.snake = Snake(self.screen_size)
        self.score = Score()
        self.death = Death(self.snake, self.score, self.screen_size)
        self.die_called = self.death.die_called

    def die_called_boolean_correct_in_the_beginning(self):
        #?
        self.death.die_called = False
        self.death.die()
        self.assertTrue(self.death.die_called)

    def screen_works(self):
        #?
        self.screen = None

    def die_call_rendering(self):
        #?
        pass

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

    def gameover_loop_do_mouse_buttons_work(self):
        #?
        game_loop = GameLoop()
        game_loop.gameover_loop()
        if self.keyboard_events == pygame.MOUSEBUTTONDOWN:
            self.assertEqual()