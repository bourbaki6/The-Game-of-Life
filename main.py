from core.grid import Grid
from simulation.engine import Simulation
from world.boundaries import ToroidalBoundary
from world.patterns import Spaceships


def print_grid(grid: Grid):
    
    for row in grid.data:
        print("".join("█" if c else "·" for c in row))
    
    print()


if __name__ == "__main__":
    
    grid = Grid.from_pattern(Spaceships.glider(), (20, 40))
    sim  = Simulation(grid, ToroidalBoundary())

    for _ in range(10):
        sim.tick()
        print(f"t = {sim.t}  alive={sim.grid.alive_count()}  status={sim.status()}")

    print_grid(sim.grid)