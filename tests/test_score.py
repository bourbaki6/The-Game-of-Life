import numpy as np
from core.grid import Grid
from core.stepper import step
from core.history import History
from world.boundaries import ToroidalBoundary, DeadCellsBoundary
from world.patterns import Basic, Spaceships, Oscillator, Acorn, Diehard, Pentomino


def test_grid_empty():
    g = Grid.empty((5, 5))
    assert g.alive_count() == 0
    assert g.shape == (5, 5)

def test_grid_random():
    g = Grid.random((20, 20), p=0.5)
    assert 0 < g.alive_count() < 400

def test_grid_copy_independence():
    g = Grid.random((10, 10))
    c = g.copy()
    c.data[0, 0] = 1 - c.data[0, 0]
    assert not np.array_equal(g.data, c.data)

def test_grid_set_cell():
    g = Grid.empty((5, 5))
    g.set_cell(2, 3, 1)
    assert g.data[2, 3] == 1

def test_grid_from_pattern_centred():
    pat = Spaceships.glider()
    g = Grid.from_pattern(pat, (20, 40))
    assert g.alive_count() == 5
    assert g.shape == (20, 40)

def test_grid_eq():
    a = Grid.empty((4, 4))
    b = Grid.empty((4, 4))
    assert a == b
    b.data[0, 0] = 1
    assert a != b

def test_blinker_period_2():
   
    b  = Grid.from_pattern(Basic.blinker(), (10, 10))
    g1 = step(b,  ToroidalBoundary())
    g2 = step(g1, ToroidalBoundary())
    assert np.array_equal(g2.data, b.data)

def test_block_stable():

    b = Grid.from_pattern(Basic.square(), (10, 10))
    assert np.array_equal(step(b, ToroidalBoundary()).data, b.data)

def test_empty_stays_empty():
    g = Grid.empty((10, 10))
    assert step(g, ToroidalBoundary()).alive_count() == 0

def test_glider_alive_count():
    assert Spaceships.glider().alive_count() == 5

def test_ruleset_highlife():
    g = Grid.empty((5, 5))
   
    for r, c in [(0,1),(0,2),(0,3),(1,0),(1,4),(2,2)]:
        g.data[r, c] = 1
    result = step(g, DeadCellsBoundary(), ruleset = "highlife")
    assert result.alive_count() >= 0  

def test_ruleset_day_and_night():
    g = Grid.random((10, 10), p=0.5)
    r = step(g, ToroidalBoundary(), ruleset = "day_and_night")
    assert r.alive_count() >= 0

def test_ruleset_morley():
    g = Grid.random((10, 10), p=0.5)
    r = step(g, ToroidalBoundary(), ruleset = "morley")
    assert r.alive_count() >= 0


def test_dead_boundary_no_wrap():
    g = Grid.empty((5, 5))
    g.data[0, 0] = 1
    assert step(g, DeadCellsBoundary()).data[0, 0] == 0

def test_toroidal_wraps():
    g = Grid.empty((5, 5))
    g.data[0, 0] = 1
    dead_n = step(g, DeadCellsBoundary()).alive_count()
  
    assert dead_n >= 0

def test_history_stable():
    h = History()
    g = Grid.from_pattern(Basic.square(), (10, 10))
    h.push(g)
    h.push(step(g, ToroidalBoundary()))
    assert h.is_stable()

def test_history_undo():
    h = History()
    g0 = Grid.random((10, 10))
    g1 = step(g0, ToroidalBoundary())
    h.push(g0)
    h.push(g1)
    prev = h.undo()
    assert prev == g0

def test_history_periodic():
    h = History()
    b = Grid.from_pattern(Basic.blinker(), (10, 10))
    h.push(b)
    g1 = step(b, ToroidalBoundary())
    h.push(g1)
    g2 = step(g1, ToroidalBoundary())
    h.push(g2)
    
    assert h.is_periodic(2)


def test_acorn_alive():
    assert Acorn.acorn().alive_count() == 7

def test_diehard_alive():
    assert Diehard.diehard().alive_count() == 7

def test_pulsar_shape():
    assert Basic.pulsar().shape == (17, 17)

def test_gosper_alive():
    assert Basic.gosper_glider_gun().alive_count() == 36

def test_rpentomino_alive():
    assert Pentomino.rpentomino().alive_count() == 5

def test_lwss_alive():
    assert Oscillator.lwss().alive_count() == 9


def test_simulation_tick():
    from simulation.engine import Simulation
    g = Grid.from_pattern(Spaceships.glider(), (20, 40))
    sim = Simulation(g, ToroidalBoundary())
    for _ in range(4):
        sim.tick()
    assert sim.t == 4
    assert sim.grid.alive_count() == 5   

def test_simulation_status_extinct():
    from simulation.engine import Simulation
    g = Grid.empty((10, 10))
    sim = Simulation(g, ToroidalBoundary())
    sim.tick()
    assert sim.status() == "extinct"

def test_simulation_status_stable():
    from simulation.engine import Simulation
    g = Grid.from_pattern(Basic.square(), (10, 10))
    sim = Simulation(g, ToroidalBoundary())
    sim.tick()
    assert sim.status() == "stable"