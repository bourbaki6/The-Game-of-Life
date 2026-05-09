

import numpy as np
from core.grid import Grid
from core.history import History

class StateDetector:

    def __init__(self, history: History):
        self.history = history

    def classify(self, grid: Grid) -> str:

        if grid.alive_count() == 0:
            return "extinct"
        
        if self.history.is_stable():
            return "still life"
        
        if self.history.is_periodic(2):
            return "oscillator (p2)"
        
        if self.history.is_periodic(3):
            return "oscillator (p3)"
        
        return "active"