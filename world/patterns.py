import numpy as np
from core.grid import Grid

class Basic:

    @staticmethod
    def square() -> Grid:
        data = np.array([
            [1, 1],
            [1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def diagonal() -> Grid:
        data = np.array([
            [0, 1],
            [1, 0]
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
    def tablecloth() -> Grid:
        data = np.array([
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
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
    def domino() -> Grid:
        data = np.array([
            [1, 1]
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
    def obospark() -> Grid:
        data = np.array([
            [1, 0, 1]
        ], data = np.uint8)
        return Grid(data)
    
    @staticmethod
    def bipond() -> Grid:
        data = np.array([
            [0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 0],
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
        ], dtype = np.uint8)
        return Grid(data)

    @staticmethod
    def pulsar() -> Grid:
        data = np.zeros((17, 17), dtype=np.uint8)
        cols = [2, 3, 4, 10, 11, 12]
        rows_top = [0, 5, 7, 12]
        for r in rows_top:
            for c in cols:
                data[r][c] = 1
        rows_left = [2, 3, 4, 10, 11, 12]
        cols_side = [0, 5, 7, 12]
        for r in rows_left:
            for c in cols_side:
                data[r][c] = 1
        return Grid(data)
    
    @staticmethod
    def arrow() -> Grid:
        data = np.array([
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)

    @staticmethod
    def gosper_glider_gun() -> Grid:
        data = np.zeros((11, 38), dtype=np.uint8)
        
        cells = [
            (0,24),(1,22),(1,24),(2,12),(2,13),(2,20),(2,21),(2,34),(2,35),
            (3,11),(3,15),(3,20),(3,21),(3,34),(3,35),(4,0),(4,1),(4,10),
            (4,16),(4,20),(4,21),(5,0),(5,1),(5,10),(5,14),(5,16),(5,17),
            (5,22),(5,24),(6,10),(6,16),(6,24),(7,11),(7,15),(8,12),(8,13)
        ]
       
        for r, c in cells:
            data[r][c] = 1
        return Grid(data)

class Pentomino:

    @staticmethod
    def tpentomino() -> Grid:
        data = np.array([
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)
     
    @staticmethod
    def rpentomino() -> Grid:
        data = np.array([
            [0, 1, 1],
            [1, 1, 0],
            [0, 1, 0]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def qpentomino() -> Grid:
        data = np.array([
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def zpentomino() -> Grid:
        data = np.array([
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 1]
        ], dtype = np.uint8)
        return Grid(data)

 
class Spaceships:

    @staticmethod
    def quad() -> Grid:
        data = np.array([
            [1, 1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1, 1]
        ], dtype = np.uint8)
        return Grid(data)
    
    @staticmethod
    def glider() -> Grid:
        data = np.array([
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ], dtype = np.uint8)
        return Grid(data)

class Oscillator:

    @staticmethod
    def toad() -> Grid:
        
        data = np.array([
            [0, 1, 1, 1],
            [1, 1, 1, 0]
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

class Acorn:
    
    @staticmethod
    def acorn() -> Grid:
        data = np.array([
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0,0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1]
        ], dtype = np.uint8)

        return Grid(data)
    
class Diehard:

    @staticmethod
    def diehard() -> Grid:
        data = np.array([
            [0,0,0,0,0,0,1,0],
            [1,1,0,0,0,0,0,0],
            [0,1,0,0,0,1,1,1]
        ], dtype = np.uint8)
        return Grid(data)

class Ant:

    @staticmethod
    def ant() -> Grid:
        data = np.array([
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 0, 0]
        ], dtype = np.uint8)
        return Grid(data)
    
class Decapole:

    @staticmethod
    def decapole() -> Grid:
        data = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], dtype = np.uint8)
        return Grid(data)