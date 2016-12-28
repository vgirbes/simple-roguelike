import unittest
import Components
from DungeonGenerator import Dungeon

from Entity import Entity

class TestDungeonGenerator(unittest.TestCase):
    def test_init_default_dungeon(self):
        dungeon = Dungeon()
        
        self.assertEqual(len(dungeon.cells), 80 * 50)

        for cell in dungeon.cells:
            self.assertEqual(cell.components['render'].char, '#')

    def test_init_custom_dungeon(self):
        width = 12
        height = 23

        dungeon = Dungeon(width, height)

        self.assertEqual(len(dungeon.cells), width * height)

    def test_dig_rect(self):
        dungeon = Dungeon()

        x = 3
        y = 5
        w = 25
        h = 40

        unfilledChar = '#'
        filledChar = '.'
        
        dungeon.dig_rect(x, y, w, h)

        xRange = range(x, x + w)
        yRange = range(y, y + h)

        for cell in dungeon.cells:
            cellPos = cell.components['position']
            cellRender = cell.components['render']

            if cellPos.x in xRange and cellPos.y in yRange:
                self.assertEqual(cellRender.char, filledChar)
            else:
                self.assertEqual(cellRender.char, unfilledChar)

    def test_create_default_rooms(self):
        dungeon = Dungeon()

        defaultMinRooms = dungeon.minRooms
        defaultMaxRooms = dungeon.maxRooms

        dungeon.create_rooms()

        self.assertTrue(defaultMinRooms <= len(dungeon.rooms) <= defaultMaxRooms)

    def test_create_custom_rooms(self):
        dungeon = Dungeon()

        dungeon.minRooms = 2
        dungeon.maxRooms = 4

        dungeon.create_rooms(minRooms, maxRooms)

        self.assertTrue(minRooms <= len(dungeon.rooms) <= maxRooms)

    def test_get_random_cell(self):
        wDungeon = 20
        hDungeon = 15

        dungeon = Dungeon(wDungeon, hDungeon)
        cell = dungeon.get_random_cell()

        cellPos = cell.components['position']

        self.assertTrue(0 <= cellPos.x <= wDungeon)
        self.assertTrue(0 <= cellPos.y <= hDungeon)

    def test_get_cell_by_position(self):
        wDungeon = 20
        hDungeon = 15

        dungeon = Dungeon(wDungeon, hDungeon)

        x = 5
        y = 12

        cell = dungeon.get_cell_by_position(x, y)
        self.assertEqual(cell.components['position'].x, x)
        self.assertEqual(cell.components['position'].y, y)

        cell = dungeon.get_cell_by_position(0, 0)
        self.assertEqual(cell.components['position'].x, 0)
        self.assertEqual(cell.components['position'].y, 0)

        lastPosX = wDungeon - 1
        lastPosY = hDungeon - 1

        cell = dungeon.get_cell_by_position(lastPosX, lastPosY)
        self.assertEqual(cell.components['position'].x, lastPosX)
        self.assertEqual(cell.components['position'].y, lastPosY)
