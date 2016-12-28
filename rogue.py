from Components import *
from Entity import Entity
from Systems import RenderSystem
from DungeonGenerator import Dungeon

entities = []

minX = 0
maxX = 10

minY = 0
maxY = 8

for x in range(minX, maxX):
    for y in range(minY, maxY):
        if x == minX or x == maxX - 1 or y == minY or y == maxY - 1:
            char = '#'
            name = 'wall'
        else:
            char = '.'
            name = 'floor'
        
        newEnt = Entity(name)
        newEnt.add_component(Render(char))
        newEnt.add_component(Position(x, y))

        entities.append(newEnt)
    

hero = Entity('rogue')
hero.add_component(Render('@'))
hero.add_component(Position(3, 5))

entities.append(hero)

renderSystem = RenderSystem()

dungeon = Dungeon()
dungeon.create_rooms()

while True:
    renderSystem.pre_update()
    renderSystem.update(dungeon.cells)
    renderSystem.post_update()
