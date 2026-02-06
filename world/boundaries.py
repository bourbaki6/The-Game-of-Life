#---general topology of the world---#

#---1. Dead outside of boundary---#
#---2. Mobius strips---#
#---3. Toroidal strips---#

import numpy as np

class Boundary:

    def count_neighbour_cells(self, data: np.ndarray) -> np.ndarray:
        raise NotImplementedError
    
class DeadCellsBoundary:

    def count_neighbour_cells(self, data: np.ndarray) -> np.ndarray:
        n = np.zeros_like(data)

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                n += np.roll(np.roll(data, dx, axis=0), dy, axis=1)
        return n
        

class MobiusStrip:

    def count_neighbors(self, data: np.ndarray) -> np.ndarray:
        h, w = data.shape
        n = np.zeros_like(data)

        for i in range(h):
            for j in range(w):
                count = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < h and 0 <= nj < w:
                            count += data[ni, nj]
                n[i, j] = count
        return n


class ToroidalBoundary:
    def count_neighbors(self, data: np.ndarray) -> np.ndarray:
        h, w = data.shape
        n = np.zeros_like(data)

        for i in range(h):
            for j in range(w):
                count = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue

                        ni, nj = i + dx, j + dy

                        if ni < 0 or ni >= h:
                            continue

                        if nj < 0:
                            nj = w - 1
                            ni = h - 1 - ni
                        elif nj >= w:
                            nj = 0
                            ni = h - 1 - ni

                        count += data[ni, nj]

                n[i, j] = count
        return n
