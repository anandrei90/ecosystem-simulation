"""
plant.py — defines the Plant subclass of Entity.

Plants are stationary entities that can grow over time.
For now, we only define structure and placeholder methods.
"""

from typing import Tuple
from .entity import Entity


class Plant(Entity):
    """Represents a plant in the ecosystem."""

    # TODO: validate inputs with Pydantic
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

    def grow(self) -> None:
        """Increase plant size by 1."""
        self.size += 1

    def update(self) -> None:
        """
        Update plant state for each time step (currently does nothing).
        """
        # TODO: handle growth, decay etc.
        pass
