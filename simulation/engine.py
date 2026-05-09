#---time evoltion observation---#

from core.stepper import step
from core.grid import Grid
from world.boundaries import Boundary


class Simulation:

    def __init__(self, grid: Grid, boundary: Boundary):
        self.grid = grid
        self.boundary = boundary
        self.t = 0


    def tick(self):
        
        counts = self.boundary.count_neighbors(self.grid.data)
        self.grid = step(self.grid, counts)
        self.t += 1
        return self.grid