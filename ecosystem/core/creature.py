"""
creature.py — defines the Creature subclass of Entity.

Creatures are moving entities capable of movement, feeding, and reproduction.
For now, we only define structure and placeholder methods.
"""

from typing import Tuple, TYPE_CHECKING
from ecosystem.core.entity import Entity

# import Environment only for type checking purposes and not at runtime
# avoids potential circular imports in the future
if TYPE_CHECKING:
    from ecosystem.core.environment import Environment


class Creature(Entity):
    """Represents a creature in the ecosystem."""

    def __init__(
        self,
        position: Tuple[int, int],
        env: "Environment",
        energy: float = 100.0
    ):
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
        super().__init__(position, env)
        self.energy: float = energy
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
