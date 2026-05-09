#---The grid world of teh game represented through numpy arrays, just teh state prsent here---#


import numpy as np
from typing import Tuple

class Grid:
    
    def __init__(self, data: np.ndarray):
        
        if data.ndim != 2:
            raise ValueError("Grid is 2D")
        self.data = data.astype(np.uint8)

    @property
    def shape(self): return self.data.shape

    def alive_count(self) -> int:
        return int(self.data.sum())

    def set_cell(self, row: int, col: int, value: int):
        self.data[row, col] = value

    @classmethod
    def from_pattern(cls, pattern: np.ndarray, canvas: tuple, center=True) -> 'Grid':
        grid = cls.empty(canvas)
        h, w = pattern.shape
        r, c = (canvas[0]//2 - h//2, canvas[1]//2 - w//2) if center else (0, 0)
        grid.data[r:r+h, c:c+w] = pattern
        
        return grid
    
