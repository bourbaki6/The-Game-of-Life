#---applying rules to grid---#

from core.rules import Rules
from core.grid import Grid

import numpy as np

def step(grid:Grid, neighbour_counts: np.ndarray) -> Grid:

    data = grid.data
    
    h, w = data.shape
    new = np.zeros_like(data)

    new = np.where(
        (data == 1) & np.isin(neighbour_counts, [2, 3]), 1,
        np.where((data == 0) & (neighbour_counts == 3), 1, 0)
    ).astype(np.unit8)
    
    return Grid(new)


