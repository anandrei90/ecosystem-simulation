import unittest
from ecosystem.simulation.simulator import Simulation
from ecosystem.core.environment import Environment
from ecosystem.core.plant import Plant
from ecosystem.core.creature import Creature


class TestSimulation(unittest.TestCase):
    """Unit tests for the Simulation class."""

    def setUp(self):
        """Create a simple environment with a plant and a creature."""
        self.env = Environment(width=5, height=5)
        self.plant = Plant(position=(0, 0))
        self.creature = Creature(position=(1, 1), energy=50)

        self.env.add_entity(self.plant)
        self.env.add_entity(self.creature)

    def tearDown(self):
        """Clean up environment and entities after each test."""
        del self.env
        del self.plant
        del self.creature

    # TODO: add tests


if __name__ == "__main__":
    unittest.main()
