import unittest
from ecosystem.core.creature import Creature


class TestCreature(unittest.TestCase):
    """Tests for the Creature class."""

    # TODO later: add tearDown() method

    def setUp(self):
        """Instantiate a Creature entity for testing."""
        self.creature = Creature(position=(5, 10), energy=70)

    def test_entity_initialization(self):
        """Creature should initialize with correct attributes."""
        self.assertIsInstance(self.creature.id, str)
        self.assertEqual(self.creature.position, (5, 10))
        self.assertTrue(self.creature.alive)
        self.assertEqual(self.creature.age, 0)
        self.assertEqual(self.creature.energy, 70)

    def test_creature_movement(self):
        """Checks behaviour of move() method."""
        # to expand when move() gets expanded
        pass

    def test_creature_eating(self):
        """Checks behaviour of eat() method."""
        # to expand when eat() gets expanded
        pass

    def test_creature_reproduction(self):
        """Checks behaviour of reproduce() method."""
        # to expand when reproduce() gets expanded
        pass

    def test_creature_update(self):
        """Checks behaviour of update() method."""
        # to expand when update() gets expanded
        old_age = self.creature.age
        self.creature.update()
        self.assertEqual(self.creature.age, old_age + 1)

    def test_repr_contains_useful_info(self):
        """String representation should include class name and position."""
        rep = repr(self.creature)
        self.assertIn("Creature", rep)
        self.assertIn("(5, 10)", rep)


if __name__ == "__main__":
    unittest.main()
