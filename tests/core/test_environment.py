import unittest
from ecosystem.core.environment import Environment
from ecosystem.core.plant import Plant


class TestEnvironment(unittest.TestCase):
    """Tests for the Environment class."""

    def setUp(self):
        """
        Instantiate an Environment object and some
        entities to populate the environment.
        """
        self.env = Environment(width=10, height=20)
        self.plant1 = Plant(position=(5, 2))
        self.plant2 = Plant(position=(3, 7))
        self.plant3 = Plant(position=(1, 1))
        self.plant4 = Plant(position=(4, 6))

    def tearDown(self):
        """Delete the created objects after testing is done."""
        del self.env
        del self.plant1
        del self.plant2
        del self.plant3
        del self.plant4

    def test_environment_initialization(self):
        """Environment should initialize with correct attributes."""
        self.assertEqual(self.env.width, 10)
        self.assertEqual(self.env.height, 20)
        self.assertEqual(self.env.tick_count, 0)
        self.assertEqual(len(self.env.entity_dict), 0)

    def test_entity_addition(self):
        """Adding an entity should register it in entity_dict."""
        n_old = len(self.env.entity_dict)
        self.env.add_entity(self.plant1)
        self.assertIn(self.plant1.id, self.env.entity_dict)
        self.assertEqual(len(self.env.entity_dict), n_old + 1)

    def test_multiple_entities_addition(self):
        """Multiple entities should be tracked independently."""
        n_old = len(self.env.entity_dict)
        self.env.add_entity(self.plant1)
        self.env.add_entity(self.plant2)
        self.assertEqual(len(self.env.entity_dict), n_old + 2)
        self.assertIn(self.plant1.id, self.env.entity_dict)
        self.assertIn(self.plant2.id, self.env.entity_dict)
        self.assertNotEqual(self.plant1.id, self.plant2.id)

    def test_entity_removal(self):
        """Removing an entity should delete it from entity_dict."""
        self.env.add_entity(self.plant1)
        n_old = len(self.env.entity_dict)
        self.env.remove_entity(self.plant1)
        self.assertEqual(len(self.env.entity_dict), n_old - 1)
        self.assertNotIn(self.plant1.id, self.env.entity_dict)

    def test_tick_advances_time(self):
        """tick() should increase tick_count by one."""
        old_count = self.env.tick_count
        self.env.tick()
        self.assertEqual(self.env.tick_count, old_count + 1)

    def test_tick_shuffles_entities(self):
        """tick() should shuffle the entities."""
        # Add 4 plants to be (almost) sure shuffle produces an effect
        self.env.add_entity(self.plant1)
        self.env.add_entity(self.plant2)
        self.env.add_entity(self.plant3)
        self.env.add_entity(self.plant4)
        old_order = list(self.env.entity_dict.keys())
        self.env.tick()
        new_order = list(self.env.entity_dict.keys())
        # Order very likely to change with 4 items
        self.assertNotEqual(old_order, new_order)
        self.assertEqual(set(old_order), set(new_order))

    def test_run_advances_time_by_steps(self):
        """run(steps=N) should advance tick_count by N."""
        old_count = self.env.tick_count
        steps = 13
        self.env.run(steps=steps)
        self.assertEqual(self.env.tick_count, old_count + steps)

    def test_run_with_zero_steps(self):
        """run(steps=0) should not change tick_count."""
        old_count = self.env.tick_count
        self.env.run(steps=0)
        self.assertEqual(self.env.tick_count, old_count)

    def test_environment_reset(self):
        """Check if the environment is emptied and reset to null time."""
        self.env.add_entity(self.plant1)
        self.env.run(steps=9)
        self.env.reset()
        self.assertEqual(self.env.tick_count, 0)
        self.assertEqual(len(self.env.entity_dict), 0)


if __name__ == "__main__":
    unittest.main()
