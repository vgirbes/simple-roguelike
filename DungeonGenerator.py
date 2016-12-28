import random

from Components import *
from Entity import Entity

class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w - 1
        self.y2 = y + h - 1

    def intersect(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

    def get_random_point(self):
        # Excluding first&last row&column
        x = random.randint(self.x1, self.x2 - 1)
        y = random.randint(self.y1, self.y2 - 1)

        return {'x': x, 'y': y}

class Dungeon:
    wallChar = '#'
    floorChar = '.'
    minRooms = 15
    maxRooms = 20

    def __init__(self, width = 80, height = 50):
        self.cells = []
        self.rooms = []

        self.width = width
        self.height = height

        # We won't use cells on the first and last rows and columns of the map, 
        # hence the starting cell is 1 instead of 0 and the last cell is width or height - 2
        self.firstCellX = 1 
        self.firstCellY = 1
        self.lastCellX = self.width - 2
        self.lastCellY = self.height - 2

        self.fill_with_walls()

    def fill_with_walls(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                cell = Entity()
                cell.add_component(Render(self.wallChar))
                cell.add_component(Position(x, y))

                self.cells.append(cell)

    def create_rooms(self):
        numOfRooms = random.randint(self.minRooms, self.maxRooms)

        while len(self.rooms) < numOfRooms:
            room = self.create_room()

            if room:
                self.rooms.append(room)

    def create_room(self, wMin = 5, wMax = 20, hMin = 5, hMax = 20):
        firstCell = self.get_random_cell()
        firstCellPos = firstCell.components['position']

        w = random.randint(wMin, wMax) 
        h = random.randint(hMin, hMax)

        room = Rect(firstCellPos.x, firstCellPos.y, w, h)

        # Prevent rooms to go outside of the map
        if (room.x2 >= self.lastCellX or room.y2 >= self.lastCellY
           or self.is_overlapping_room(room)):
                return False

        for x in range(room.x1, room.x2):
            for y in range(room.y1, room.y2):
                cell = self.get_cell_by_position(x, y)
                cell.components['render'].char = self.floorChar

        lenRooms = len(self.rooms)

        if lenRooms > 0:
            self.create_corridor(self.rooms[lenRooms - 1] , room)

        return room

    def is_overlapping_room(self, newRoom):
        for room in self.rooms:
            if room.intersect(newRoom):
                return True

        return False

    def create_corridor(self, fromRoom, toRoom):
        fromPoint = fromRoom.get_random_point()
        xFrom = fromPoint['x']
        yFrom = fromPoint['y']

        toPoint = toRoom.get_random_point()
        xTo = toPoint['x']
        yTo = toPoint['y']

        xRange = range(xFrom, xTo + 1)
        yRange = range(yFrom, yTo + 1)

        # Range not operating well on negatives
        if xFrom > xTo:
            xRange = range(xTo, xFrom + 1)
        if yFrom > yTo:
            yRange = range(yTo, yFrom + 1)
        
        for x in xRange:
            cell = self.get_cell_by_position(x, yFrom)
            cell.components['render'].char = self.floorChar

        for y in yRange:
            cell = self.get_cell_by_position(xTo, y)
            cell.components['render'].char = self.floorChar

    def get_random_cell(self):
        x = random.randint(self.firstCellX, self.lastCellX)
        y = random.randint(self.firstCellY, self.lastCellY)

        return self.get_cell_by_position(x, y)

    def get_cell_by_position(self, x, y):
        for cell in self.cells:
            position = cell.components['position']

            if position.x == x and position.y == y:
                return cell
