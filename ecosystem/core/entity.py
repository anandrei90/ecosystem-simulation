"""
entity.py — defines the base class for all ecosystem entities.

Each entity has a unique ID, a position within the environment,
and an `update()` method that defines how it behaves each tick.
"""

from abc import ABC, abstractmethod
from typing import Tuple
import uuid


class Entity(ABC):

    """Abstract base class for all entities in the ecosystem."""

    def __init__(self, position: Tuple[int, int]) -> None:
        """
        Initialize a new entity.

        Parameters:
        ----------
        position: Tuple[int, int]
            (x, y) coordinates of the entity.
        """
        # unique ID attributed at creation
        self.id: str = str(uuid.uuid4())
        self.position: Tuple[int, int] = position
        self.alive: bool = True

    # enforces the update method for all subclasses
    @abstractmethod
    def update(self) -> None:
        """Defines behaviour of the entity for a simulation time step."""
        pass

    def __repr__(self) -> str:
        """Return a string representation for debugging."""
        return f"{self.__class__.__name__}(id={self.id[:8]}, \
            pos={self.position})"
