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
        self.assertFalse(self.sim.verbose)

    @unittest.expectedFailure
    def test_negative_ticks_raises_error(self):
        """
        Initializing a Simulation with negative number of steps should
        throw an error.
        """
        Simulation(environment=self.env, max_ticks=-1)

    def test_simulation_runs_till_end(self):
        """Simulation should run for `max_ticks` time steps."""
        self.sim.run()
        self.assertEqual(self.env.tick_count, self.sim.max_ticks)

    def test_verbose_true_works(self):
        """Simulation should run without error when verbose=True."""
        self.sim = Simulation(environment=self.env, verbose=True)
        try:
            self.sim.run()
        except Exception as e:
            self.fail(
                f"Simulation.run() raised an exception with verbose=True: {e}"
                )


if __name__ == "__main__":
    unittest.main()
