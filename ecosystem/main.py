from ecosystem.simulation.simulator import Simulation
from ecosystem.core.environment import Environment
from ecosystem.core.plant import Plant
from ecosystem.core.creature import Creature


def build_environment() -> Environment:
    """Create an environment and populate it with initial entities."""
    env = Environment(width=10, height=10)

    # Add plants
    env.add_entity(Plant(position=(2, 3)))
    env.add_entity(Plant(position=(9, 5)))

    # Add creatures
    env.add_entity(Creature(position=(3, 1), energy=100))
    env.add_entity(Creature(position=(7, 7), energy=100))

    return env


def main():
    env = build_environment()

    # Configure and run simulation
    sim = Simulation(
        environment=env,
        max_ticks=20,
        verbose=True,
    )

    sim.run()

    print(f"Simulation complete. Final tick count: {env.tick_count}")


if __name__ == "__main__":
    main()
