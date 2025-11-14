
from ecosystem.core.environment import Environment


class Simulation:
    """
    High-level simulation controller.
    Responsible for orchestrating environment ticks and controlling runtime.
    """
    # TODO: take care of step_size <= 0
    def __init__(
        self,
        environment: Environment,
        max_ticks: int = 20,
        step_size: int = 5,
        verbose: bool = False
    ):
        self.environment = environment
        self.max_ticks = max_ticks
        self.step_size = step_size
        self.verbose = verbose

    def run(self) -> None:
        """Run the simulation until `max_ticks` is reached."""
        while self.environment.tick_count < self.max_ticks:
            self.environment.run(steps=self.step_size)
            if self.verbose:
                print(f"Tick {self.environment.tick_count}/{self.max_ticks}")
