#---general topology of the world---#

#---1. Dead outside of boundary---#
#---2. Mobius strips---#
#---3. Toroidal strips---#


import numpy as np

class DeadCellsBoundary:

    def count_neighbors(self, data: np.ndarray) -> np.ndarray:
        
        n = np.zeros_like(data)
        
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                n += np.roll(np.roll(data, dx, axis=0), dy, axis=1)
        return n

class ToroidalBoundary:

    def count_neighbors(self, data: np.ndarray) -> np.ndarray:
       
        n = np.zeros_like(data)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                rolled = np.roll(np.roll(data, dx, axis=0), dy, axis=1)
                n += rolled
        return n

class MobiusStrip:
    def count_neighbors(self, data: np.ndarray) -> np.ndarray:
        
        h, w = data.shape
        n = np.zeros_like(data)
        
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                shifted = np.roll(data, dx, axis=0)
              
                if dx != 0:
                    shifted = np.flip(shifted, axis=1)
                rolled = np.roll(shifted, dy, axis=1)
                n += rolled
        return n