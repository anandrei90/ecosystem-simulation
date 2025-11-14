import unittest
from ecosystem.core.entity import Entity


# Dummy subclass for testing abstract base class functionality
class DummyEntity(Entity):

    def update(self):
        # Minimal implementation to satisfy ABC requirements
        return True


class TestEntity(unittest.TestCase):
    """Tests for the base Entity abstract class."""

    def setUp(self):
        """Instantiate a dummy entity for testing."""
        self.entity = DummyEntity(position=(5, 10))

    def test_entity_initialization(self):
        """Entity should initialize with correct attributes."""
        self.assertIsInstance(self.entity.id, str)
        self.assertEqual(self.entity.position, (5, 10))
        self.assertTrue(self.entity.alive)

    def test_entity_update_contract(self):
        """Ensure update method of subclass can be called."""
        result = self.entity.update()
        self.assertTrue(result)

    def test_entity_is_abstract(self):
        """Verify Entity cannot be instantiated directly."""
        with self.assertRaises(TypeError):
            Entity(position=(0, 0))

    def test_repr_contains_useful_info(self):
        """String representation should include class name and position."""
        rep = repr(self.entity)
        self.assertIn("DummyEntity", rep)
        self.assertIn("(5, 10)", rep)


if __name__ == "__main__":
    unittest.main()
