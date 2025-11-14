"""
simulator.py - defines the Simulation class.

A simulation takes care of time evolution inside an environment.
"""

from ecosystem.core.environment import Environment


class Simulation:
    """
    High-level simulation controller.
    Responsible for orchestrating environment ticks and controlling runtime.
    """
    def __init__(
        self,
        environment: Environment,
        max_ticks: int = 20,
        verbose: bool = False
    ):
        """
        Initialize a simulation.

        Parameters:
        ----------
        environment: Environment
            Environment to be simulated.
        max_ticks: int
            Number ot time steps of the simulations. Must be at least 1.
        verbose: bool
            Controls verbosity of the simulation.
        """
        self.environment = environment
        if max_ticks >= 1:
            self.max_ticks = max_ticks
        else:
            raise ValueError("Step size should be greater than or equal to 1.")
        self.verbose = verbose

    def run(self) -> None:
        """Run the simulation until `max_ticks` is reached."""
        while self.environment.tick_count < self.max_ticks:
            self.environment.tick()
            if self.verbose:
                print(f"Tick {self.environment.tick_count}/{self.max_ticks}")
