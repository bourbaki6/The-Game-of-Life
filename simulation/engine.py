#---time evoltion observation---#

import numpy as np
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
    
    def is_stable(self) -> bool:
        return np.array_equal(self.grid.data, self._prev)

    def is_extinct(self) -> bool:
        
        return self.grid.alive_count() == 0