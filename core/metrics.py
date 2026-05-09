
import numpy as np
from core.grid import Grid
from dataclasses import dataclass

@dataclass
class GridMetrics:
    
    alive: int
    density: float        
    bbox: tuple           
    centre_of_mass: tuple 


def compute(grid: Grid) -> GridMetrics:
    data = grid.data
    alive = int(data.sum())
    total = data.size
    density = alive / total if total else 0.0

    coords = np.argwhere(data)
    
    if coords.size:
        bbox = (int(coords[:,0].min()), 
                int(coords[:,1].min()),
                int(coords[:,0].max()), 
                int(coords[:,1].max()))
        
        centre = (float(coords[:,0].mean()), 
                  float(coords[:,1].mean()))
    
    else:
        bbox = (0, 0, 0, 0)
        centre = (0.0, 0.0)

    return GridMetrics(alive, density, bbox, centre)