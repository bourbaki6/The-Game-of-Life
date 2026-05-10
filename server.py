import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, PlainTextResponse

from pydantic import BaseModel
from typing import List, Literal
from dataclasses import dataclass
import numpy as np

from core.grid import Grid
from core.history import History
from core.metrics import compute
from simulation.engine import Simulation
from world.boundaries import ToroidalBoundary, DeadCellsBoundary, MobiusStrip
from world.seeder import Seeder
from world.patterns import (
    Basic, Pentomino, Spaceships, Oscillator, Acorn, Diehard, Ant, Decapole, Mozart
)

app = FastAPI(title = "Conway's Game of Life")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@dataclass
class AppState:
    sim: Simulation | None = None
    generation: int = 0
    last_pattern: str = "random"
    last_boundary: str = "toroidal"
    last_ruleset: str = "conway"

state = AppState()

def _require_sim():
    if state.sim is None:
        raise HTTPException(400, "Call /init first")

class InitRequest(BaseModel):
    cols:     int = 120
    rows:     int = 80
    pattern:  Literal[
        "random", "clustered", "symmetric", "sparse", "dense",
        "glider", "pulsar", "gosper", "rpentomino", "tpentomino",
        "acorn", "diehard", "lwss", "toad", "beacon",
        "bipond", "beehive", "ant", "decapole", "mozart",
        "infinite_growth", "mwss",
    ] = "random"
    boundary: Literal["toroidal", "dead", "mobius"] = "toroidal"
    ruleset:  Literal["conway", "highlife", "day_and_night", "morley"] = "conway"

class TickRequest(BaseModel):
    steps: int = 1

class SetCellsRequest(BaseModel):
    cells: List[List[int]]   

class LoadRLERequest(BaseModel):
    rle: str

class GridState(BaseModel):
    cols: int
    rows: int
    generation: int
    alive: int
    density: float
    status: str
    cells: List[int]

class MetricsResponse(BaseModel):
    alive: int
    density:  float
    bbox: List[int]
    bbox_area: int
    centre_of_mass: List[float]
    status: str

INFINITE_GROWTH = [
    (0,0),(0,1),(0,2),(0,4),(1,0),(2,3),(2,4),(3,1),(3,2),(3,4),(4,0),(4,2)
]

MWSS = [
    (0,1),(0,2),(0,3),(0,4),(0,5),
    (1,0),(1,5),
    (2,5),
    (3,0),(3,4),
    (4,2),
]

def _boundary(name: str):
    return {"toroidal": ToroidalBoundary,
            "dead": DeadCellsBoundary,
            "mobius": MobiusStrip}[name]()

def _embed(pattern: Grid, rows: int, cols: int) -> Grid:
    return Grid.from_pattern(pattern, (rows, cols))

def _stamp_coords(coords, rows, cols):
    g = Grid.empty((rows, cols))
    cr, cc = rows // 2, cols // 2
    for r, c in coords:
        nr, nc = cr + r, cc + c
        if 0 <= nr < rows and 0 <= nc < cols:
            g.data[nr, nc] = 1
    return g

def _grid_state() -> GridState:
    g = state.sim.grid
    rows, cols = g.shape
    alive = g.alive_count()
    density = alive / g.data.size
    return GridState(
        cols = cols, 
        rows = rows,
        generation = state.generation,
        alive = alive,
        density = density,
        status = state.sim.status(),
        cells = g.data.flatten().tolist(),
    )


def _make_grid(pattern: str, rows: int, cols: int) -> Grid:
    p = pattern
    if   p == "random":         
        return Seeder.uniform((rows, cols))
    elif p == "clustered":       
        return Seeder.clustered((rows, cols))
    elif p == "symmetric":      
        return Seeder.symmetric((rows, cols))
    elif p == "sparse":         
        return Seeder.uniform((rows, cols), p = 0.06)
    elif p == "dense":          
        return Seeder.uniform((rows, cols), p = 0.40)
    elif p == "glider":         
        return _embed(Spaceships.glider(), rows, cols)
    elif p == "pulsar":         
        return _embed(Basic.pulsar(), rows, cols)
    elif p == "gosper":          
        return _embed(Basic.gosper_glider_gun(), rows, cols)
    elif p == "rpentomino":      
        return _embed(Pentomino.rpentomino(), rows, cols)
    elif p == "tpentomino":      
        return _embed(Pentomino.tpentomino(), rows, cols)
    elif p == "acorn":          
        return _embed(Acorn.acorn(), rows, cols)
    elif p == "diehard":       
        return _embed(Diehard.diehard(), rows, cols)
    elif p == "lwss":           
        return _embed(Oscillator.lwss(), rows, cols)
    elif p == "toad":            
        return _embed(Oscillator.toad(), rows, cols)
    elif p == "beacon":         
        return _embed(Basic.beacon(), rows, cols)
    elif p == "bipond":          
        return _embed(Basic.bipond(), rows, cols)
    elif p == "beehive":        
        return _embed(Basic.beehive(), rows, cols)
    elif p == "ant":            
        return _embed(Ant.ant(), rows, cols)
    elif p == "decapole":        
        return _embed(Decapole.decapole(), rows, cols)
    elif p == "mozart":         
        return _embed(Mozart.mozart(), rows, cols)
    elif p == "infinite_growth": 
        return _stamp_coords(INFINITE_GROWTH, rows, cols)
    elif p == "mwss":            
        return _stamp_coords(MWSS, rows, cols)
    else:
        raise HTTPException(400, f"Unknown pattern: {p}")


@app.post("/init", response_model=GridState)
def init(req: InitRequest):
    state.last_pattern = req.pattern
    state.last_boundary = req.boundary
    state.last_ruleset = req.ruleset
    state.generation = 0

    grid = _make_grid(req.pattern, req.rows, req.cols)
    boundary = _boundary(req.boundary)
    state.sim = Simulation(grid, boundary, ruleset=req.ruleset)
    return _grid_state()


@app.post("/tick", response_model=GridState)
def tick(req: TickRequest):
    _require_sim()
    for _ in range(req.steps):
        state.sim.tick()
        state.generation += 1
    return _grid_state()


@app.post("/set_cells", response_model = GridState)
def set_cells(req: SetCellsRequest):
    _require_sim()
    rows, cols = state.sim.grid.shape
    for row, col, value in req.cells:
        if 0 <= row < rows and 0 <= col < cols:
            state.sim.grid.set_cell(row, col, value)
    return _grid_state()


@app.get("/state", response_model = GridState)
def get_state():
    _require_sim()
    return _grid_state()


@app.post("/reset", response_model = GridState)
def reset():
  
    _require_sim()
    g = state.sim.grid
    rows, cols = g.shape
    grid = _make_grid(state.last_pattern, rows, cols)
    boundary = _boundary(state.last_boundary)
    state.sim = Simulation(grid, boundary, ruleset = state.last_ruleset)
    state.generation = 0
    return _grid_state()


@app.post("/undo", response_model=GridState)
def undo():
    _require_sim()
    prev = state.sim.history.undo()
    if prev is None:
        raise HTTPException(400, "Nothing to undo")
    state.sim.grid = prev
    state.generation = max(0, state.generation - 1)
    return _grid_state()


@app.get("/metrics", response_model=MetricsResponse)
def metrics():
    _require_sim()
    m = compute(state.sim.grid)
    rmin, cmin, rmax, cmax = m.bbox
    area = (rmax - rmin + 1) * (cmax - cmin + 1) if m.alive > 0 else 0
    return MetricsResponse(
        alive = m.alive,
        density = m.density,
        bbox = list(m.bbox),
        bbox_area = area,
        centre_of_mass = list(m.centre_of_mass),
        status = state.sim.status(),
    )


@app.post("/load_rle", response_model =GridState)
def load_rle(req: LoadRLERequest):
    _require_sim()
    try:
        rows, cols = state.sim.grid.shape
        pattern = _parse_rle(req.rle)
        state.sim.grid = Grid.from_pattern(pattern, (rows, cols))
        state.generation = 0
        state.sim.history = History()
        state.sim.history.push(state.sim.grid)
    except Exception as e:
        raise HTTPException(400, f"Invalid RLE: {e}")
    return _grid_state()


@app.get("/export_rle")
def export_rle():
    _require_sim()
    return PlainTextResponse(_to_rle(state.sim.grid))

def _to_rle(grid: Grid, name: str = "conway_export") -> str:
    data = grid.data
    rows, cols = data.shape
    lines = [f"#N {name}", f"x = {cols}, y = {rows}, rule = B3/S23"]
    body  = []
    for row in data:
        count, char, run = 1, None, ""
        for cell in row:
            c = "o" if cell else "b"
            if c == char:
                count += 1
            else:
                if char:
                    run += (str(count) if count > 1 else "") + char
                char, count = c, 1
        run += (str(count) if count > 1 else "") + char + "$"
        body.append(run)
    return "\n".join(lines) + "\n" + "".join(body).rstrip("$") + "!"


def _parse_rle(rle: str) -> Grid:
    lines = [l for l in rle.strip().splitlines() if not l.startswith("#")]
    body  = "".join(lines[1:]).rstrip("!")
    rows_data, count_str, current_row = [], "", []
    for ch in body:
        if ch.isdigit():
            count_str += ch
        elif ch in ("b", "o"):
            n = int(count_str) if count_str else 1
            current_row.extend([0 if ch == "b" else 1] * n)
            count_str = ""
        elif ch == "$":
            n = int(count_str) if count_str else 1
            for _ in range(n):
                rows_data.append(current_row)
                current_row = []
            count_str = ""
    if current_row:
        rows_data.append(current_row)
    width = max((len(r) for r in rows_data), default=1)
    data  = np.array([r + [0] * (width - len(r)) for r in rows_data], dtype=np.uint8)
    return Grid(data)


FRONTEND = os.path.join(os.path.dirname(__file__), "frontend")
if os.path.isdir(FRONTEND):
    app.mount("/static", StaticFiles(directory=FRONTEND), name="static")

    @app.get("/")
    def index():
        return FileResponse(os.path.join(FRONTEND, "index.html"))