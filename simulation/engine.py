    
# --- Time evolution and observation ---#

from core.stepper import step
from core.grid import Grid
from core.history import History
from world.boundaries import Boundary


class Simulation:

    def __init__(self, grid: Grid, boundary: Boundary, ruleset: str = "conway"):
        
        self.grid = grid
        self.boundary = boundary
        self.ruleset = ruleset
        self.t = 0
        self._prev: Grid | None = None
        self.history = History(maxlen = 10)
        self.history.push(grid)

    def tick(self) -> Grid:
        self._prev = self.grid.copy()
        self.grid = step(self.grid, self.boundary, self.ruleset)
        self.t += 1
        self.history.push(self.grid)
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
       
        if self.history.is_periodic(2):
            return "oscillator (p2)"
       
        if self.history.is_periodic(3):
            return "oscillator (p3)"
       
        return "active"