import unittest
from snake import Snake
from death import Death
from score import Score
from gameloop import GameLoop

class TestDeath(unittest.TestCase):
    def setUp(self):
        self.game_loop = GameLoop()
        self.screen_size = self.game_loop.screen_size
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
        self.assertFalse(self.snake.dead)
        self.assertFalse(self.death.die_called)
        self.assertFalse(self.death.call_main)
