import numpy as np
from core.grid import Grid

class Patterns:
    
    @staticmethod
    def square() -> Grid:
        data = np.array([
            [1, 1],
            [1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def block() -> Grid:
        data = np.array([
            [1, 1],
            [1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def blinker() -> Grid:
        data = np.array([
            [1],
            [1],
            [1]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def ship() -> Grid:
        data = np.array([
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def beehive() -> Grid:
        data = np.array([
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def tub() -> Grid:
        data = np.array([
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def beacon() -> Grid:
        data = np.array([
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        ],  dtype = np.uint8)
        return Grid(data)

class Shapeships:


    @staticmethod
    def glider() -> Grid:
        data = np.array([
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def toad() -> Grid:
        data = np.array([
            [0, 1, 1, 1],
            [1, 1, 1, 0],
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def lwss() -> Grid:
        data = np.array([
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)
