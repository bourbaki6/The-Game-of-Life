
import numpy as np

from core.grid import Grid
from core.stepper import step
from core.history import History
from world.boundaries import ToroidalBoundary, DeadCellsBoundary
from world.patterns import Patterns, Spaceships

def test_blinker_period_2():
    
    b = Patterns.blinker()          
    g1 = step(b, ToroidalBoundary())
    g2 = step(g1, ToroidalBoundary()) 
    assert np.array_equal(g2.data, b.data)

def test_block_stable():
    
    b = Patterns.block()
    assert np.array_equal(step(b, ToroidalBoundary()).data, b.data)

def test_empty_stays_empty():
    
    g = Grid.empty((10, 10))
    assert step(g, ToroidalBoundary()).alive_count() == 0

def test_dead_boundary_no_wrap():
   
    g = Grid.empty((5, 5))
    g.data[0, 0] = 1
    result = step(g, DeadCellsBoundary())
    assert result.data[0, 0] == 0

def test_history_stable():
    h = History()
    g = Patterns.block()
    h.push(g)
    h.push(step(g, ToroidalBoundary()))
    assert h.is_stable()

def test_glider_alive_count():
    assert Spaceships.glider().alive_count() == 5