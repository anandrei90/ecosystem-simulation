# Ecosystem Simulation — OOP Project

A small object-oriented ecosystem simulation written in Python. [work in progress]

The project models entities that act and move within an evolving environment, focusing on clean design, modularity, and full unit-test coverage.

All the commands appearing below should be run from the project’s root directory.

---

## Features

* **Entity System:**
  The `Entity` class is an abstract base class. It defines the shared interface for all ecosystem objects.
The current concrete subclasses are `Plant` (immobile entity) and `Creature` (moving entity), each implementing their own behavior.

* **Environment Manager:**
  Holds all entities, performs simulation ticks, shuffles processing order, and maintains global state.

* **Utility Functions:**
  Includes various helper functions and constants.

* **Unit Tests:**
  Built with Python’s `unittest` framework, covering:

  * Entity behavior
  * Environment logic
  * Simulation logic
  * Utility functions

---

## Running the Simulation

```bash
python3 -m ecosystem.main
```

Control the simulation by creating an environment, adding entities, and running tick loops inside `main.py`.

---

## Running Tests

```bash
python3 -m unittest discover -s tests
```

---

## Future Improvements

* Additional entity behavior types
* Interaction mechanics (e.g., creature eats plant, reproduction)
* Spatial modeling enhancements
* Visualization or logging tools
* Configurable simulation parameters
* Mutation dynamics
* Reinforcement Learning: AI agents controlling entity behaviour
