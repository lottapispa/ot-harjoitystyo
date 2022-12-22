import unittest
import pygame
from fonts import Fonts
from score import Score

class TestDeath(unittest.TestCase):
    def setUp(self):
        self.score = Score()

    def test_rendering_text(self):
        fonts = Fonts()
        old = fonts.game_over
        fonts.rendering_text(self.score)
        new = fonts.game_over
        self.assertNotEqual(old, new)