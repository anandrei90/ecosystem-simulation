"""
environment.py — defines the Environment class.

The enviroment is a 2D space where various entities can evolve
and interact with each other.
"""

from typing import Dict, Tuple
from ecosystem.utils.helpers import shuffle_dictionary


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
        self.tick_count: int = 0  # Keep track of elapsed time
        self.entity_dict: Dict = {}  # Holds all active entities
        # self.is_running: bool = False  # Maybe needed later?

    def in_bounds(self, position: Tuple[int, int]) -> bool:
        """
        Checks if a certain 2D position (x, y) lies inside the environment.
        """
        x, y = position
        return 1 <= x <= self.width and 1 <= y <= self.height

    def entity_coordinates(self, entity_type) -> None:
        pass

    def add_entity(self, entity) -> None:
        """Add an entity to the environment."""

        # check if entity is spawned within bounds
        if not self.in_bounds(entity.position):
            raise IndexError("Entity placed outside of the environment.")

        # assign env parameter to created entity
        entity.env = self
        # add entity to dictionary
        self.entity_dict.update({entity.id: entity})

    def remove_entity(self, entity) -> None:
        """Remove an entity from the environment."""
        if entity.id in self.entity_dict:
            self.entity_dict.pop(entity.id)

    def tick(self) -> None:
        """Advance the simulation by one time step."""

        for entity_id in self.entity_dict:
            self.entity_dict[entity_id].update()  # update all entities

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
