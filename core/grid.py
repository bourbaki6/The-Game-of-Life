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

    def set_cell(self, row: int, col: int, value: int):
        self.data[row, col] = int(value)

    @classmethod
    def from_pattern(cls, pattern: "Grid", canvas: tuple) -> "Grid":
        g = cls.empty(canvas)
        ph, pw = pattern.shape
        r0 = max(0, (canvas[0] - ph) // 2)
        c0 = max(0, (canvas[1] - pw) // 2)
        g.data[r0:r0+ph, c0:c0+pw] = pattern.data
        
        return g

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Grid): 
            return NotImplemented
        
        return np.array_equal(self.data, other.data)

    def __repr__(self) -> str:
        r, c = self.shape
        return f"Grid({r}×{c}, alive={self.alive_count()})"

    @classmethod
    def from_pattern(cls, pattern: np.ndarray, canvas: tuple, center=True) -> 'Grid':
        
        grid = cls.empty(canvas)
        h, w = pattern.shape
        r, c = (canvas[0]//2 - h//2, canvas[1]//2 - w//2) if center else (0, 0)
        grid.data[r:r+h, c:c+w] = pattern
        
        return grid
    
