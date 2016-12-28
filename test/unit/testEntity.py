import unittest
from mock import Mock
from Entity import Entity

class TestEntityMethods(unittest.TestCase):
    def test_create_with_name_should_have_name(self):
        name = 'testEntity'
        entity = Entity(name)

        self.assertEqual(entity.name, name)

    def test_create_without_name_should_have_default_name(self):
        entity = Entity()

        self.assertEqual(entity.name, 'UnnamedEntity')

    def test_should_always_have_uid(self):
        entity = Entity()

        self.assertNotEqual(entity.uid, None)
        entity2 = Entity('test')
        self.assertNotEqual(entity2.uid, None)

    def test_add_component_should_have_component(self):
        entity = Entity()
        comp1 = Mock()
        comp2 = Mock()
        comp1.name = 'comp1'
        comp2.name = 'comp2'

        self.assertEqual(len(entity.components), 0)
        entity.add_component(comp1)
        self.assertEqual(len(entity.components), 1)
        entity.add_component(comp2)
        self.assertEqual(len(entity.components), 2)

    def test_remove_component_should_not_have_component(self):
        entity = Entity()
        comp1 = Mock()
        comp2 = Mock()
        comp1.name = 'comp1'
        comp2.name = 'comp2'

        entity.add_component(comp1)
        entity.add_component(comp2)

        entity.remove_component(comp1)
        self.assertEqual(len(entity.components), 1)
        entity.remove_component(comp2)
        self.assertEqual(len(entity.components), 0)

    def test_component_should_be_accesible(self):
        entity = Entity()
        comp = Mock()
        comp.name = 'mock'

        entity.add_component(comp)

        self.assertEqual(entity.components['mock'], comp)

if __name__ == '__main__':
    unittest.main()
