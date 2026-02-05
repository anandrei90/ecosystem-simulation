"""
plant.py — defines the Plant subclass of Entity.

Plants are stationary entities that can grow over time.
For now, we only define structure and placeholder methods.
"""

from typing import Tuple
from ecosystem.core.entity import Entity


class Plant(Entity):
    """Represents a plant in the ecosystem."""

    def __init__(self, position: Tuple[int, int]):
        """
        Initialize a new plant of size 1.

        Parameters:
        ----------
        position: Tuple[int, int]
            (x, y) coordinates of the entity.
        """
        super().__init__(position)
        self.size: int = 1  # metric for plant growth
        self.max_size = 10

    def grow(self) -> None:
        """Increase plant size by 1."""
        self.size += 1

    def get_eaten(self) -> None:
        """
        Controls what happens when a plant gets eaten.
        """
        self.size -= 1

    def update(self) -> None:
        """
        Update plant state for each time step.
        """
        if self.size < self.max_size:
            self.grow()
