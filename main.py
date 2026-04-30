
from core.grid import Grid
from simulation.engine import Simulation
from render.renderer import Renderer
from world.boundaries import ToroidalBoundary
from world.patterns import Glider

import numpy as np

def embed(pattern: Grid, shape=(60, 60)) -> Grid:

    data = np.zeros(shape, dtype = np.uint8)
    h, w = pattern.shape
    cx, cy = shape[0] // 2, shape[1] // 2
    data[cx: cx+h, cy: cy+w] = pattern.data
    return Grid(data)


if __name__ == "__main__":

    grid = embed(Glider.glider())
    sim = Simulation(grid, ToroidalBoundary())
    renderer = Renderer(sim.grid)

    while True:
        sim.tick()
        renderer.draw(sim.grid)
