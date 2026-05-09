

from collections import deque
import numpy as np
from core.grid import Grid

class History:
    def __init__(self, maxlen: int = 10):
        self._buf = deque(maxlen = maxlen)

    
    def push(self, grid: Grid):
        self._buf.append(grid.data.copy())

    
    def is_stable(self) -> bool:
        if len(self._buf) < 2: 
            return False

        return np.array_equal(self._buf[-1], self._buf[-2])

    def is_periodic(self, period: int = 2) -> bool:

        if len(self._buf) < period + 1: 
            return False
        
        return np.array_equal(self._buf[-1], self._buf[-(period+1)])

    def undo(self) -> Grid | None:

        if len(self._buf) < 2: 
            return None
        
        self._buf.pop()

        return Grid(self._buf[-1].copy())