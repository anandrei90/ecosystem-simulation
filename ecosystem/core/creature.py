"""
creature.py — defines the Creature subclass of Entity.

Creatures are moving entities capable of movement, feeding, and reproduction.
For now, we only define structure and placeholder methods.
"""

from typing import Tuple
from .entity import Entity


class Creature(Entity):
    """Represents a creature in the ecosystem."""

    # TODO: validate inputs with Pydantic
    def __init__(self, position: Tuple[int, int], energy: float = 100.0):
        super().__init__(position)
        self.energy: float = energy  # for moving/reproduction
        self.age: int = 0

    def move(self) -> None:
        """Placeholder for future movement logic."""
        pass

    def eat(self) -> None:
        """Placeholder for future eating behaviour."""
        pass

    def reproduce(self) -> None:
        """Placeholder for future reproducing behaviour."""
        pass

    def update(self) -> None:
        """
        Update creature state for each time step.
        """
        # TODO: handle movement, eating, reproduction
        self.age += 1
