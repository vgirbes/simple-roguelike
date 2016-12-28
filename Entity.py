from uuid import uuid4

class Entity:
    def __init__(self, name = None):
        self.name = name if name else 'UnnamedEntity'
        self.uid = uuid4()
        self.components = {}

    def add_component(self, component):
        self.components[component.name] = component

    def remove_component(self, component):
        self.components.pop(component.name)
