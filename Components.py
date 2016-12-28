class Position:
    def __init__(self, x, y):
        self.name = 'position'
        self.x = x
        self.y = y

class Render:
    def __init__(self, char):
        self.name = 'render'
        self.char = char

class Health:
    def __init__(self, max):
        self.name = 'health'
        self.maxHealth = max
        self.current = max

class Terrain:
    def __init__(self, passable):
        self.name = 'terrain'
        self.passable = passable
