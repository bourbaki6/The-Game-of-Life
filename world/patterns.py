import numpy as np
from core.grid import Grid

class Patterns:
    
    def square() -> Grid:
        data = np.array([
            [1, 1],
            [1, 1]
        ], dtype = np.uint8)
        return Grid(data)
     
    def block() -> Grid:
        data = np.array([
            [1, 1],
            [1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    def blinker() -> Grid:
        data = np.array([
            [1],
            [1],
            [1]
        ], dtype = np.uint8)
        return Grid(data)
    
    def ship() -> Grid:
        data = np.array([
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    def beehive() -> Grid:
        data = np.array([
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)
    
    def tub() -> Grid:
        data = np.array([
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)
    
    def beacon() -> Grid:
        data = np.array([
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        ],  dtype = np.uint8)
        return Grid(data)

class Glider:
    def glider() -> Grid:
        data = np.array([
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    def toad() -> Grid:
        data = np.array([
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 0, 0]
        ], dtype = np.uint8)
        return Grid(data)
    
    def lwss() -> Grid:
        data = np.array([
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)
