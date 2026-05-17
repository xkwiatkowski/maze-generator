import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from grid import Grid
from kruskal import kruskal
from visualizer import Visualizer

def main():
    rows, cols = 20, 20
    cell_size = 30

    grid = Grid(rows, cols)
    steps = kruskal(grid)

    vis = Visualizer(grid, cell_size=cell_size)
    vis.animate(steps, delay_ms=30)

if __name__ == "__main__":
    main()