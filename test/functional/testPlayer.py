import unittest

from Components import *
from Entity import Entity

class TestPlayerCreation(unittest.TestCase):
    def setUp(self):
        self.initialPosX = 0
        self.initialPosY = 0
        self.char = '@'
        
        self.player = Entity('player')
        self.player.add_component(Render(self.char))
        self.player.add_component(Position(self.initialPosX, self.initialPosY))

    def test_initial_pos_is_setted_up(self):
        self.assertEqual(self.player.components['position'].x, self.initialPosX);
        self.assertEqual(self.player.components['position'].y, self.initialPosY);

    def test_char_is_correct(self):
        self.assertEqual(self.player.components['render'].char, self.char);

    def test_change_position(self):
        newPosX = 3
        newPosY = 5

        self.player.components['position'].x += newPosX
        self.player.components['position'].y += newPosY

        self.assertEqual(self.player.components['position'].x, newPosX)
        self.assertEqual(self.player.components['position'].y, newPosY)
