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
        self._prev: Grid | None = None

    def tick(self) -> Grid:
        self._prev = self.grid.copy()
        self.grid = step(self.grid, self.boundary)
        self.t += 1
        
        return self.grid

    @property
    def is_stable(self) -> bool:
        return self._prev is not None and self.grid == self._prev

    @property
    def is_extinct(self) -> bool:
        return self.grid.alive_count() == 0

    def status(self) -> str:
        if self.is_extinct: 
            return "extinct"
        
        if self.is_stable:  
            return "stable"
        
        return "active"