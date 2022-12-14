import unittest
from snake import Snake
from food import Food
from keyboard_events import KeyboardEvents
from score import Score
from gameloop import GameLoop
import pygame

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.gameloop = GameLoop()
        self.snake = Snake(self.gameloop.screen_size)
        self.score = Score()
        self.length = self.snake.length
        self.color = self.snake.color
        self.screen_size = self.snake.screen_size
        self.location = self.snake.location
        self.directions = self.snake.directions
        self.counter = self.snake.counter
        self.step = self.snake.step
        self.dead = self.snake.dead
        self.keyboard_events = KeyboardEvents().get()

    def test_correct_length_in_the_beginning(self):
        self.assertEqual(self.length, 1)

    def test_correct_color(self):
        self.assertEqual(self.color, (102, 205, 0))

    def test_correct_screen(self):
        self.assertEqual(self.screen_size[0], 640)
        self.assertEqual(self.screen_size[1], 480)

    def test_correct_directions(self):
        self.assertEqual(self.directions["up"], (0, -1))
        self.assertEqual(self.directions["down"], (0, 1))
        self.assertEqual(self.directions["left"], (-1, 0))
        self.assertEqual(self.directions["right"], (1, 0))

    def test_correct_step_size(self):
        self.assertEqual(self.step, 20)

    def test_head_location(self):
        #tests that head_location function works
        self.assertEqual(self.snake.head_location(), self.snake.location[0])

    def test_head_rect(self):
        #checks rectangle is the right size
        self.a, self.b, self.c, self.d = self.snake.head_rect()
        self.assertTupleEqual((self.c, self.d), (20, 20))

    # checks if direction changes
    def test_turn_up(self):
        snake = Snake(self.gameloop.screen_size)
        snake.direction = snake.directions["left"]
        snake.length == 2
        snake.turn_up()
        self.assertTupleEqual(snake.direction, (0, -1))

    def test_turn_down(self):
        snake = Snake(self.gameloop.screen_size)
        snake.direction = snake.directions["right"]
        snake.length == 2
        snake.turn_down()
        self.assertTupleEqual(snake.direction, (0, 1))

    def test_turn_left(self):
        snake = Snake(self.gameloop.screen_size)
        snake.direction = snake.directions["down"]
        snake.length == 2
        snake.turn_left()
        self.assertTupleEqual(snake.direction, (-1, 0))

    def test_turn_right(self):
        snake = Snake(self.gameloop.screen_size)
        snake.direction = snake.directions["left"]
        snake.length == 1
        snake.turn_right()
        self.assertTupleEqual(snake.direction, (1, 0))

    def test_move_changes_head_location_x(self):
        self.location = [(40, 40)]
        self.direction = self.snake.directions["up"]
        self.old_head_location = self.snake.head_location()
        self.snake.move()
        self.new_head_location = self.snake.head_location()
        self.assertNotEqual(self.old_head_location, self.new_head_location)

    def test_move_changes_head_location_y(self):
        self.location = [(40, 40)]
        self.direction = self.snake.directions["left"]
        self.old_head_location = self.snake.head_location()
        self.snake.move()
        self.new_head_location = self.snake.head_location()
        self.assertNotEqual(self.old_head_location, self.new_head_location)

    def test_move_changes_tail_location_x(self):
        #check that tail of snake moves as well so that snake doesn't just grow when moving
        self.location = [(40, 40)]
        self.direction = self.snake.directions["up"]
        self.old_tail_location = self.snake.location[-1]
        self.snake.move()
        self.new_tail_location = self.snake.location[-1]
        self.assertNotEqual(self.old_tail_location, self.new_tail_location)

    def test_move_changes_tail_location_y(self):
        #check that tail of snake moves as well so that snake doesn't just grow when moving
        self.location = [(40, 40)]
        self.direction = self.snake.directions["left"]
        self.old_tail_location = self.snake.location[-1]
        self.snake.move()
        self.new_tail_location = self.snake.location[-1]
        self.assertNotEqual(self.old_tail_location, self.new_tail_location)

    def test_eating_and_move_grows_location_list(self):
        # checks if function eating works with function move to grow snake
        food = Food()
        food.location = (40, 40)
        snake = Snake(self.gameloop.screen_size)
        snake.location = [(40, 40)]
        snake.direction = snake.directions["up"]
        score = Score()
        score.eating(snake, food)
        snake.move()
        self.assertEqual(len(snake.location), 2)

    def test_dies_when_touches_wall_x(self):
        snake = Snake(self.gameloop.screen_size)
        snake.location = [(640, 240)]
        snake.direction = self.directions["down"]
        snake.move()
        self.assertTrue(snake.dead)

    def test_dies_when_touches_wall_y(self):
        snake = Snake(self.gameloop.screen_size)
        snake.location = [(340, 480)]
        snake.direction = self.directions["down"]
        snake.move()
        self.assertTrue(snake.dead)

    def test_dies_when_touches_itself(self): 
        snake = Snake(self.gameloop.screen_size)
        snake.location = [(360, 220), (360, 200), (380, 200), (400, 200), (400, 220), (400, 240), (380, 240), (360, 240), (340, 240), (320, 240)]
        snake.direction = self.directions["down"]
        snake.move()
        self.assertTrue(snake.dead)

    def test_draw_snake_counter_in_the_beginning(self):
        snake = Snake(self.gameloop.screen_size)
        self.counter = snake.counter
        self.assertEqual(self.counter, 0)

    def test_draw_snake_len_1(self):
        snake = Snake(self.gameloop.screen_size)
        gameloop = GameLoop()
        snake.counter = 0
        snake.length = 1
        snake.location = [(340, 280)]
        snake.draw_snake(gameloop.screen)
        self.assertEqual(snake.rect, pygame.Rect((340, 280), (20, 20)))
        self.assertEqual(snake.counter, 1)

    def test_draw_snake_longer(self):
        snake = Snake(self.gameloop.screen_size)
        gameloop = GameLoop()
        snake.counter = 0
        snake.length = 2
        snake.location = [(340, 280), (360, 280)]
        snake.draw_snake(gameloop.screen)
        self.assertEqual(snake.rect, pygame.Rect((360, 280), (20, 20)))
        self.assertEqual(snake.counter, 2)
