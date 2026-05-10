
# --- Applying rules to the grid (vectorised) ---#

import numpy as np
from core.grid import Grid
from world.boundaries import Boundary

RULESETS = {
    "conway": (lambda c, n: np.where(c == 1, np.isin(n, [2, 3]), n == 3)),
    "highlife": (lambda c, n: np.where(c == 1, np.isin(n, [2, 3]), np.isin(n, [3, 6]))),
    "day_and_night":(lambda c, n: np.where(c == 1, np.isin(n, [3,4,6,7,8]), np.isin(n, [3,6,7,8]))),
    "morley": (lambda c, n: np.where(c == 1, np.isin(n, [2,4,5]),    np.isin(n, [3,6,8]))),
}

def step(grid: Grid, boundary: Boundary, ruleset: str = "conway") -> Grid:
    counts = boundary.count_neighbors(grid.data)
    rule = RULESETS.get(ruleset, RULESETS["conway"])
    new = rule(grid.data, counts).astype(np.uint8)
    return Grid(new)