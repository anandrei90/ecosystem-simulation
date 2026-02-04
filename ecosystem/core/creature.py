"""
creature.py — defines the Creature subclass of Entity.

Creatures are moving entities capable of movement, feeding, and reproduction.
For now, we only define structure and placeholder methods.
"""

from typing import Tuple
from ecosystem.core.entity import Entity


class Creature(Entity):
    """Represents a creature in the ecosystem."""

    def __init__(self, position: Tuple[int, int], energy: float = 100.0):
        """
        Initialize a new creature of age 0.

        Parameters:
        ----------
        position: Tuple[int, int]
            (x, y) coordinates of the entity.
        energy: float
            Controls ability to move and reproduce.
            Get replenished through eating.
        """
        super().__init__(position)
        self.energy: float = energy
        self.age: int = 0

    def move(self, dx: int, dy: int) -> None:
        """
        Moves the creature from (x, y) to (x+dx, y+dy).
        """
        self.position = (self.position[0] + dx, self.position[1] + dy)

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
