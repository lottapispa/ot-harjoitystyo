import unittest
from snake import Snake
from food import Food
from gameloop import GameLoop
from death import Death
from score import Score
from keyboard_events import KeyboardEvents
import pygame

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

    def keyboard_keys_works(self):
        #?
        gameloop = GameLoop()
        snake = Snake(self.screen_size)
        snake.direction = self.snake.directions["left"]
        snake.length = 2
        for self.event in gameloop.events.get():
            self.event.type == pygame.KEYDOWN
            self.event.key == pygame.K_UP

        for self.test_event in gameloop.events.get():
            self.test_event.type == pygame.KEYDOWN
            self.test_event.key == pygame.K_UP

        gameloop.keyboard()
        self.assertTupleEqual(snake.direction, (0, -1))
    
    def keyboard_exit_works(self):
        #?
        gameloop = GameLoop()
        snake = Snake(self.screen_size)
        snake.direction = self.snake.directions["left"]
        snake.length = 2
        for self.event in gameloop.events.get():
            self.event.type == pygame.QUIT
        gameloop.keyboard()
        self.assertTupleEqual()

    def main(self):
        #?
        game_loop = GameLoop()
        
    def snake_dies(self):
        #?
        game_loop = GameLoop()
        True
        self.snake.dead = True
        game_loop.main()
        self.assertTrue(self.death.die_called)
