"""
environment.py — defines the Environment class.

The enviroment is a 2D space where various entities can evolve
and interact with each other.
"""

from typing import Dict, Tuple, Set, TYPE_CHECKING
from ecosystem.utils.helpers import shuffle_dictionary

if TYPE_CHECKING:
    from ecosystem.core.entity import Entity


class Environment:
    """A 2D space where entities evolve and interact."""

    def __init__(self, width: int, height: int):
        """
        Initialize an empty simulation environment.

        Parameters:
        ----------
        width: int
            Extent of the environment along the x-axis.
        height: int
            Extent of the environment along the y-axis.
        """
        self.width: int = width
        self.height: int = height
        self.tick_count: int = 0  # keep track of elapsed time
        # holds all active entities as {entity.id: entity}
        self.entity_dict: Dict[str, Entity] = {}
        # holds entity positions as {(x, y): {entity_1.id, entity_2.id, ...}}
        self.entities_at: Dict[Tuple[int, int], Set[str]] = {}
        # self.is_running: bool = False  # Maybe needed later?

    def in_bounds(self, position: Tuple[int, int]) -> bool:
        """
        Checks if a certain 2D position (x, y) lies inside the environment.
        """
        x, y = position
        return 1 <= x <= self.width and 1 <= y <= self.height

    def update_position_dict(
            self,
            position: Tuple[int, int],
            entity_id: str
    ) -> None:
        """
        Updates the position dictionary to reflect the addition of an entity
        to the environment.
        """
        if position in self.entities_at:
            self.entities_at[position].add(entity_id)
        else:
            self.entities_at.update({position: {entity_id}})

    def move_entity(
            self,
            entity_id: str,
            old_position: Tuple[int, int],
            new_position: Tuple[int, int]
    ) -> None:
        """
        Updates the position dictionary to reflect the movement of an entity.
        """
        self.entities_at[old_position].remove(entity_id)
        self.update_position_dict(new_position, entity_id)

    def add_entity(self, entity: Entity) -> None:
        """Add an entity to the environment."""

        # check if entity is spawned within bounds
        if not self.in_bounds(entity.position):
            raise IndexError("Entity placed outside of the environment.")

        # assign env parameter to created entity
        entity.env = self
        # add entity to dictionary
        self.entity_dict.update({entity.id: entity})
        # add entity id to position dictionary
        self.update_position_dict(entity.position, entity.id)

    def remove_entity(self, entity: Entity) -> None:
        """Remove an entity from the environment."""
        if entity.id in self.entity_dict:
            self.entity_dict.pop(entity.id)
            self.entities_at[entity.position].remove(entity.id)

    def tick(self) -> None:
        """Advance the simulation by one time step."""

        for entity_id in self.entity_dict:
            self.entity_dict[entity_id].update()  # update all entities
            # TODO: check here if alive and remove if not?

        self.tick_count += 1  # push time forward by 1 unit
        # shuffle entity order to mitigate biases
        self.entity_dict = shuffle_dictionary(self.entity_dict, seed=10)

    def run(self, steps: int) -> None:
        """Run the simulation for a fixed number of ticks."""
        for _ in range(steps):
            self.tick()

    def reset(self) -> None:
        """Reset the environment state."""
        self.entity_dict.clear()
        self.tick_count = 0
