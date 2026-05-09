from core.grid import Grid
from simulation.engine import Simulation
from world.boundaries import ToroidalBoundary
from world.patterns import Spaceships

import numpy as np

def embed(pattern: Grid, shape=(60, 60)) -> Grid:

    data = np.zeros(shape, dtype=np.uint8)
    h, w = pattern.shape        
    cx, cy = shape[0] // 2, shape[1] // 2
    data[cx: cx+h, cy: cy+w] = pattern.data
    return Grid(data)


if __name__ == "__main__":

    grid = embed(Spaceships.glider())  
    sim = Simulation(grid, ToroidalBoundary())

    for _ in range(10):
        sim.tick()
        print(f"t={sim.t}  alive={sim.grid.alive_count()}")