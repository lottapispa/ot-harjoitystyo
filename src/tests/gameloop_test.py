import unittest
from snake import Snake
from food import Food
from gameloop import GameLoop
from keyboard_events import KeyboardEvents
import random
import sys
import pygame

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.screen_width = GameLoop().screen_width
        self.screen_height = GameLoop().screen_height
        #self.screen = GameLoop().screen
        self.font = GameLoop().font
        self.bigfont = GameLoop().bigfont

    def test_correct_screen(self):
        self.assertEqual(self.screen_width, 640)
        self.assertEqual(self.screen_height, 480)
        #self.assertEqual(self.screen, (640, 480))

    def correct_fonts(self):
        # 
        self.assertEqual(self.font, pygame.font.SysFont("Candara", 24))
        self.assertEqual(self.bigfont, pygame.font.SysFont("Candara", 36))

    def gameover_loop(self):
        pass