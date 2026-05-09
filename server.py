
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pydantic import BaseModel
from typing import List, Literal, Optional
import numpy as np

from core.grid import Grid
from simulation.engine import Simulation
from world.boundaries import ToroidalBoundary, DeadCellsBoundary, MobiusStrip
from world.patterns import Patterns, Spaceships

app = FastAPI(title = "Conway's Game of Life")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

sim: Optional[Simulation] = None
generation: int = 0


class InitRequest(BaseModel):
    cols: int = 120
    rows: int = 80
    pattern: Literal["random", "glider", "pulsar", "gosper", "rpentomino"] = "random"
    boundary: Literal["toroidal", "dead", "mobius"] = "toroidal"

class TickRequest(BaseModel):
    steps: int = 1

class SetCellsRequest(BaseModel):
    cells: List[List[int]]  

class GridState(BaseModel):
    cols: int
    rows: int
    generation: int
    alive: int
    cells: List[int]


def _boundary(name: str):
    return {"toroidal": ToroidalBoundary,
            "dead": DeadCellsBoundary,
            "mobius": MobiusStrip}[name]()

def _embed(pattern: Grid, rows: int, cols: int) -> Grid:
   
    data = np.zeros((rows, cols), dtype = np.uint8)
    ph, pw = pattern.shape
    r0 = max(0, (rows - ph) // 2)
    c0 = max(0, (cols - pw) // 2)
    data[r0:r0+ph, c0:c0+pw] = pattern.data
    
    return Grid(data)

def _grid_state() -> GridState:
    g = sim.grid
    
    rows, cols = g.shape
    
    return GridState(
        cols = cols,
        rows = rows,
        generation = generation,
        alive = g.alive_count(),
        cells = g.data.flatten().tolist(),
    )

@app.post("/init", response_model = GridState)
def init(req: InitRequest):
    global sim, generation
    generation = 0

    rows, cols = req.rows, req.cols

    if req.pattern == "random":
        grid = Grid.random((rows, cols), p = 0.18)
    elif req.pattern == "glider":
        grid = _embed(Spaceships.glider(), rows, cols)
    elif req.pattern == "pulsar":
        grid = _embed(Patterns.pulsar(), rows, cols)
    elif req.pattern == "gosper":
        grid = _embed(Patterns.gosper_glider_gun(), rows, cols)
    elif req.pattern == "rpentomino":
        grid = _embed(Patterns.rpentomino(), rows, cols)
    else:
        raise HTTPException(400, f"Unknown pattern: {req.pattern}")

    boundary = _boundary(req.boundary)
    sim = Simulation(grid, boundary)
    return _grid_state()


@app.post("/tick", response_model=GridState)
def tick(req: TickRequest):
    global generation
    if sim is None:
        raise HTTPException(400, "Call /init first")
    for _ in range(req.steps):
        sim.tick()
        generation += 1
    return _grid_state()


@app.post("/set_cells", response_model=GridState)
def set_cells(req: SetCellsRequest):
    if sim is None:
        raise HTTPException(400, "Call /init first")
    rows, cols = sim.grid.shape
    for row, col, value in req.cells:
        if 0 <= row < rows and 0 <= col < cols:
            sim.grid.data[row, col] = value
    return _grid_state()


@app.get("/state", response_model=GridState)
def state():
    if sim is None:
        raise HTTPException(400, "Call /init first")
    return _grid_state()


FRONTEND = os.path.join(os.path.dirname(__file__), "frontend")
if os.path.isdir(FRONTEND):
    app.mount("/static", StaticFiles(directory=FRONTEND), name="static")

    @app.get("/")
    def index():
        return FileResponse(os.path.join(FRONTEND, "index.html"))