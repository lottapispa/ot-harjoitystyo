import unittest
from snake import Snake
from food import Food
from gameloop import GameLoop

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food()
        self.size = self.food.size
        self.color = self.food.color
        self.location = self.food.location
        self.game_loop = GameLoop()
        self.snake = Snake(self.game_loop.screen_size)
        self.length = self.snake.length

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

    def test_draw_food(self):
        food = Food()
        gameloop = GameLoop()
        food.location = (240, 340)
        food.draw_food(gameloop.screen)
        self.assertEqual(food.location, (240, 340))
