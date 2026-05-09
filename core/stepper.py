#---applying rules to grid---#

from core.grid import Grid
import numpy as np

from world.boundaries import Boundary

def step(grid: Grid, boundary: Boundary) -> Grid:
    
    counts = boundary.count_neighbors(grid.data)
    
    new = np.where(
        (grid.data == 1) & np.isin(counts, [2, 3]), 1,
        np.where((grid.data == 0) & (counts == 3), 1, 0)
    ).astype(np.uint8)
    
    return Grid(new)

