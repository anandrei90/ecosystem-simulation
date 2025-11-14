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
        step_size: int = 5,
        verbose: bool = False
    ):
        self.environment = environment
        self.max_ticks = max_ticks
        if step_size >= 1:
            self.step_size = step_size
        else:
            raise ValueError("Step size should be greater than or equal to 1.")
        self.verbose = verbose

    def run(self) -> None:
        """Run the simulation until `max_ticks` is reached."""
        while self.environment.tick_count < self.max_ticks:
            self.environment.run(steps=self.step_size)
            if self.verbose:
                print(f"Tick {self.environment.tick_count}/{self.max_ticks}")
