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
    from ecosystem.core.plant import Plant


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
            Gets replenished through eating.
        """
        super().__init__(position)
        self.energy: float = energy
        self.age: int = 0

    def move(self, dx: int, dy: int) -> None:
        """
        Moves the creature from (x, y) to (x+dx, y+dy) and substracts
        the energy necessary for moving.
        """
        self.position = (self.position[0] + dx, self.position[1] + dy)
        self.energy -= 2

    def eat(self, plant: "Plant") -> None:
        """
        Controls eating behaviour.
        """
        # TODO: check isinstance(plant, Plant)?
        self.energy += 10.0  # creature acquires energy by eating
        # part of the plant gets eaten
        plant.get_eaten()  # encapsulation: let Plant alter its own state

    def reproduce(self) -> None:
        """
        Creature reproduces if it has enough energy.
        """
        if self.env:  # check if env is None
            self.env.add_entity(
                Creature(position=self.position)
            )
            self.energy -= 50

    def update(self) -> None:
        """
        Update creature state for each time step.
        """
        self.age += 1  # aging
        # movement

        # TODO: write check_collision method
        # eating
        # if self.env.check_collision(self, plant: "Plant"):
        #     self.eat(plant)
        # reproduction
        if self.energy >= 150:
            self.reproduce()
