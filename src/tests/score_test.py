import unittest
from score import Score
from snake import Snake
from food import Food
from gameloop import GameLoop

class TestScore(unittest.TestCase):
    def setUp(self):
        self.game_loop = GameLoop()
        self.score = Score()
        self.food = Food()
        self.snake = Snake(self.game_loop.screen_size)
        self.points = self.score.points
        self.highscore = self.score.highscore
        self.length = self.snake.length

    def test_correct_points_in_the_beginning(self):
        self.assertEqual(self.points, 0)

    def test_correct_highscore_in_the_beginning(self):
        self.assertEqual(self.highscore, 0)

    def test_eating(self):
        snake = Snake(self.game_loop.screen_size)
        food = Food()
        score = Score()
        food.location = (40, 40)
        snake.location = [(40, 40)]
        snake.length = 4
        score.points = 3
        score.highscore = 7
        score.eating(snake, food)
        self.assertEqual(snake.length, 5)
        self.assertEqual(score.points, 4)
        self.assertEqual(score.highscore, 7)

    def test_eating_doesnt_collide(self):
        snake = Snake(self.game_loop.screen_size)
        food = Food()
        score = Score()
        food.location = (40, 40)
        snake.location = [(170, 170)]
        snake.length = 4
        score.points = 3
        score.highscore = 7
        score.eating(snake, food)
        self.assertEqual(snake.length, 4)
        self.assertEqual(score.points, 3)
        self.assertEqual(score.highscore, 7)
