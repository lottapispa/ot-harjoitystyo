import unittest
#import ohtekoodi
from snake import Snake
from food import Food
from keyboard_events import KeyboardEvents
from gameloop import GameLoop
import pygame

class TestSnake(unittest.TestCase):
    def setUp(self):
        snake = Snake()
        self.length = snake.length
        self.color = snake.color
        self.screen_width = snake.screen_width
        self.screen_height = snake.screen_height
        self.location = snake.location
        self.up = snake.up
        self.down = snake.down
        self.left = snake.left
        self.right = snake.right
        self.direction = snake.direction
        self.points = snake.points
        self.highscore = snake.highscore
        self.step = snake.step
        self.die_called = snake.die_called
        self.reset_called = snake.reset_called
        self.dead = snake.dead
        #self.events = GameLoop().events
        self.keyboard_events = KeyboardEvents().get()

    def test_correct_length_in_the_beginning(self):
        self.assertEqual(self.length, 1)

    def test_correct_color_in_the_beginning(self):
        self.assertEqual(self.color, (102, 205, 0))

    def test_correct_screen(self):
        self.assertEqual(self.screen_width, 640)
        self.assertEqual(self.screen_height, 480)

    def test_correct_directions(self):
        self.assertEqual(self.up, (0, -1))
        self.assertEqual(self.down, (0, 1))
        self.assertEqual(self.left, (-1, 0))
        self.assertEqual(self.right, (1, 0))

    def test_correct_points_in_the_beginning(self):
        # points variable is the same size as length variable
        self.assertEqual(self.points, 0)

    def test_correct_highscore_in_the_beginning(self):
        # points variable is the same size as length variable
        self.assertEqual(self.highscore, 0)

    def test_correct_step_size(self):
        self.assertEqual(self.step, 20)

    def test_head_location(self):
        #tests that head_location function works
        snake = Snake()
        self.assertEqual(snake.head_location(), snake.location[0])

    def test_death_booleans_correct_in_the_beginning(self):
        snake = Snake()
        self.assertFalse(snake.die_called)
        self.assertFalse(snake.reset_called)
        self.assertFalse(snake.dead)

    # self.direction variable is _ if condition is met
    def test_turn_up(self):
        snake = Snake()
        if self.keyboard_events == pygame.K_UP:
            self.assertEqual(snake.direction, self.up)

    def test_turn_down(self):
        snake = Snake()
        if self.keyboard_events == pygame.K_DOWN:
            self.assertEqual(snake.direction, self.down)

    def test_turn_left(self):
        snake = Snake()
        if self.keyboard_events == pygame.K_LEFT:
            self.assertEqual(snake.direction, self.left)

    def test_turn_right(self):
        snake = Snake()
        if self.keyboard_events == pygame.K_RIGHT:
            self.assertEqual(snake.direction, self.right)

    def test_move_changes_head_location(self):
        snake = Snake()
        snake.location = [(40, 40)]
        snake.direction = self.up
        self.old_head_location = snake.head_location()
        snake.move()
        self.new_head_location = snake.head_location()
        self.assertNotEqual(self.old_head_location, self.new_head_location)

    def test_move_changes_tail_location(self):
        #check that tail of snake moves as well so that snake doesn't just grow when moving
        snake = Snake()
        snake.location = [(40, 40)]
        snake.direction = self.up
        self.old_tail_location = snake.location[-1]
        snake.move()
        self.new_tail_location = snake.location[-1]
        self.assertNotEqual(self.old_tail_location, self.new_tail_location)

    def test_dies_when_touches_wall(self):
        snake = Snake()
        snake.location = [(640, 240)]
        snake.direction = self.down
        snake.move()
        self.assertTrue(snake.dead)

    def test_dies_when_touches_itself(self): 
        snake = Snake()
        snake.location = [(360, 220), (360, 200), (380, 200), (400, 200), (400, 220), (400, 240), (380, 240), (360, 240), (340, 240), (320, 240)]
        snake.direction = self.down
        snake.move()
        self.assertTrue(snake.dead)

    def test_resets_when_dies(self):
        snake = Snake()
        if snake.die_called:
            self.assertTrue(snake.reset_called)

    def test_reset_works_correctly(self):
        snake = Snake()
        snake.reset()
        self.assertTrue(snake.reset_called)
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.location, [((snake.screen_width/2), (snake.screen_height/2))])
        self.assertEqual(snake.points, 0)
        self.assertEqual(snake.highscore, 0)
        self.assertEqual(snake.duration, 0)
        self.assertFalse(snake.dead)
        self.assertFalse(snake.die_called)
