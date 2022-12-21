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
        self.snake = Snake()
        self.length = self.snake.length
        self.game_loop = GameLoop()

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
        #?
        self.game_loop = GameLoop()
        self.a, self.b, self.c, self.d = self.food.draw_food(self.game_loop.screen)
        self.assertEqual(self.b, (139,69,19))
        self.assertEqual(self.d, 10)

        