# Conway's Game of Life

A modular, real-time implementation of Conway’s Game of Life.

## Overview

This project implements Conway’s Game of Life as a modular simulation engine.
The core computation layer is fully decoupled from the API layer and UI.

The backend is built with FastAPI and streams grid state via WebSockets.
The frontend renders the simulation using HTML5 Canvas.

## Boundary Conditions

- Finite Grid
- Toroidal Topology
- Möbius Strip Topology

## Future Work

- Sparse grid optimization
- Distributed simulation nodes
- Rule editor interface
- RLE pattern import
- Multi-user sessions
- Performance profiling metrics


