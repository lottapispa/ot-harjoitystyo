import unittest
import ohtekoodi
from ohtekoodi import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.length = Snake().length
        self.color = Snake().color

    def test_oikea_pituus_alussa(self):
        self.assertEqual(self.length, 1)

    def test_oikea_vari_alussa(self):
        self.assertEqual(self.color, (102, 205, 0))

    def draw_snake(self):
        pass

    def snake_moves_on_its_own(self):
        pass

    def dies_when_touches_wall(self):
        pass

    def die(self):
        pass
