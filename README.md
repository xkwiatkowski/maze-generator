# Maze Generator

## Description
This project implements a maze generator using graph algorithms. The maze is represented as a grid graph (cells = vertices, walls = edges), and generation works by building a random spanning tree. The project includes step-by-step visualization of the algorithms and a BFS-based maze solver.

## Algorithms
- **Randomized Kruskal's Algorithm** — randomly removes walls using a Union-Find/DSU structure to avoid cycles
- **Randomized Prim's Algorithm** — grows the maze from a single starting cell by randomly expanding the frontier
- **BFS Solver** — finds the shortest path from the top-left to the bottom-right corner

## References
- https://en.wikipedia.org/wiki/Maze_generation_algorithm
- https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

## Technologies
- Python 3
- Custom implementation of graph algorithms and Union-Find structure
- Step-by-step visualization using Pygame

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Controls
- **SPACE** — pause/resume generation
- **S** — solve the maze after generation
- **Q** — quit
