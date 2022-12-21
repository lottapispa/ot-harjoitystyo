import unittest
from snake import Snake
from food import Food
from gameloop import GameLoop
from keyboard_events import KeyboardEvents
import pygame

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()
        self.food = Food()
        self.screen_width = GameLoop().screen_width
        self.screen_height = GameLoop().screen_height
        self.font = GameLoop().font
        self.bigfont = GameLoop().bigfont
        self.keyboard_events = KeyboardEvents().get()

    def test_correct_screen(self):
        self.assertEqual(self.screen_width, 640)
        self.assertEqual(self.screen_height, 480)

    def test_keyboard(self):
        pass

    def gameover_loop_do_mouse_buttons_work(self):
        #?
        game_loop = GameLoop()
        game_loop.gameover_loop()
        if self.keyboard_events == pygame.MOUSEBUTTONDOWN:
            self.assertEqual()

    def test_eating_and_move_grows_location_list(self):
        food = Food()
        food.location = (40, 40)
        snake = Snake()
        snake.location = [(40, 40)]
        snake.direction = snake.up
        food.eating(snake)
        snake.move()
        self.assertEqual(len(snake.location), 2)

    def snake_dies(self):
        #?
        game_loop = GameLoop()
        self.snake.dead = True
        game_loop.main()
        self.assertTrue(self.snake.die_called)
