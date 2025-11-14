import unittest
from ecosystem.core.plant import Plant


class TestPlant(unittest.TestCase):
    """Tests for the Plant class."""

    # TODO later: add tearDown() method

    def setUp(self):
        """Instantiate a Plant entity for testing."""
        self.plant = Plant(position=(5, 10))

    def test_entity_initialization(self):
        """Plant should initialize with correct attributes."""
        self.assertIsInstance(self.plant.id, str)
        self.assertEqual(self.plant.position, (5, 10))
        self.assertTrue(self.plant.alive)
        self.assertEqual(self.plant.size, 1)

    def test_plant_growth(self):
        """Checks behaviour of grow() method."""
        old_size = self.plant.size
        self.plant.grow()
        self.assertEqual(self.plant.size, old_size + 1)

    def test_plant_update(self):
        """Checks behaviour of update() method."""
        # to expand when update() gets expanded
        pass

    def test_repr_contains_useful_info(self):
        """String representation should include class name and position."""
        rep = repr(self.plant)
        self.assertIn("Plant", rep)
        self.assertIn("(5, 10)", rep)


if __name__ == "__main__":
    unittest.main()
