#---applying rules to grid---#

from core.rules import Rules
from core.grid import Grid

import numpy as np

def step(grid:Grid, neighbour_counts: np.ndarray) -> Grid:

    data = grid.data
    
    h, w = data.shape
    new = np.zeros_like(data)

    for i in range(h):
        for j in range(w):
            new[i, j] = life_rule(data[i, j], neighbour_counts[i, j])

    return Grid(new)


