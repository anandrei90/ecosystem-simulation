import unittest
from ecosystem.simulation.simulator import Simulation
from ecosystem.core.environment import Environment
from ecosystem.core.plant import Plant
from ecosystem.core.creature import Creature


class TestSimulation(unittest.TestCase):
    """Unit tests for the Simulation class."""

    def setUp(self):
        """
        Create a simulation of an environment containing
        a plant and a creature.
        """
        self.env = Environment(width=5, height=5)
        self.plant = Plant(position=(0, 0))
        self.creature = Creature(position=(1, 1), energy=50)

        self.env.add_entity(self.plant)
        self.env.add_entity(self.creature)
        # Might need to override self.sim in subsequent tests
        self.sim = Simulation(environment=self.env)

    def tearDown(self):
        """Clean up environment and entities after each test."""
        del self.sim
        del self.env
        del self.plant
        del self.creature

    def test_simulation_initialization(self):
        """Simulation should initialize with correct attributes."""
        self.assertEqual(self.sim.environment, self.env)
        self.assertEqual(self.sim.max_ticks, 20)
        self.assertEqual(self.sim.step_size, 5)
        self.assertFalse(self.sim.verbose)

    @unittest.expectedFailure
    def test_negative_step_size_raises_error(self):
        """
        Initializing a Simulation with negative step size should
        throw an error.
        """
        Simulation(environment=self.env, step_size=-1)

    # TODO: add tests


if __name__ == "__main__":
    unittest.main()
