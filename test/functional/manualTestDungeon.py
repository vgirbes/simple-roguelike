from Components import *
from Entity import Entity
from Systems import RenderSystem
from DungeonGenerator import Dungeon

renderSystem = RenderSystem()

dungeon = Dungeon()
dungeon.create_rooms()

while True:
    renderSystem.pre_update()
    renderSystem.update(dungeon.cells)
    renderSystem.post_update()
