# Conway's Game of Life

This is a full-stack implementation of Conway's Game of Life. The simulation runs in Python and is rendered live in the browser via a REST API.

## How it works
 
Every generation, four rules are applied simultaneously to every cell on the grid:
 
```
Underpopulation  ->  a live cell with < 2 neighbours dies
Survival         -> a live cell with 2 or 3 neighbours lives
Overpopulation   ->  a live cell with > 3 neighbours dies
Reproduction     -> a dead cell with exactly 3 neighbours is born
```
 
The Python backend computes each generation using vectorised NumPy — no cell-by-cell loops. The browser fetches the result and renders it on a canvas at ~18 generations per second.

## Quick start
 
```bash
pip install -r requirements.txt
uvicorn server:app --reload
```
 
Open **http://localhost:8000** in your browser.
 
Or run it in the terminal:
 
```bash
python main.py
```

## Rule sets
 
| Rule | Born | Survives |
|---|---|---|
| Conway | 3 | 2, 3 |
| HighLife | 3, 6 | 2, 3 |
| Day & Night | 3, 6, 7, 8 | 3, 4, 6, 7, 8 |
| Morley | 3, 6, 8 | 2, 4, 5 |

 
## Boundary types
 
| Boundary | Behaviour |
|---|---|
| Toroidal | Edges wrap — grid is a torus |
| Dead cells | Edges treated as permanently dead |
| Möbius strip | Wraps horizontally with a vertical flip |

 
