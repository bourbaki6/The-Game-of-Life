
#---controlled randomisation---#
#---this is to make initial state more interesting than
#   np.random; so that we can get structured seeds ---#

import numpy as np
from core.grid import Grid

class Seeder:
    @staticmethod
    def uniform(shape: tuple, p: float = 0.18) -> Grid:
        return Grid((np.random.random(shape) < p).astype(np.uint8))

    @staticmethod
    def clustered(shape: tuple, n_clusters: int = 8, radius: int = 6) -> Grid:
        data = np.zeros(shape, dtype=np.uint8)
        rows, cols = shape
        
        for _ in range(n_clusters):
            cr = np.random.randint(0, rows)
            cc = np.random.randint(0, cols)
            
            for r in range(max(0, cr-radius), min(rows, cr+radius)):
                for c in range(max(0, cc-radius), min(cols, cc+radius)):
                    if np.sqrt((r-cr)**2 + (c-cc)**2) < radius:
                        data[r, c] = np.random.random() < 0.55
        
        return Grid(data)

    @staticmethod
    def symmetric(shape: tuple, p: float = 0.22) -> Grid:
        
        rows, cols = shape
        half = (np.random.random((rows//2, cols//2)) < p).astype(np.uint8)
        q = np.block([[half, np.fliplr(half)],
                      [np.flipud(half), np.flipud(np.fliplr(half))]])
        return Grid(q[:rows, :cols])