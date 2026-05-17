import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from grid import Grid
from kruskal import kruskal
from prim import prim
from visualizer import Visualizer

def main():
    rows, cols = 20, 20
    cell_size = 30
    delay_ms = 30

    print("Choose a maze generation algorithm:")
    print("  1 - Randomized Kruskal's Algorithm")
    print("  2 - Randomized Prim's Algorithm")
    choice = input("Enter your choice (1 or 2): ").strip()

    grid = Grid(rows, cols)

    if choice == '1':
        steps = kruskal(grid)
        algorithm_name = "Kruskal's Algorithm"
    elif choice == '2':
        steps = prim(grid)
        algorithm_name = "Prim's Algorithm"
    else:
        print("Invalid choice. Please run the program again and select either 1 or 2.")
        return

    vis = Visualizer(grid, cell_size=cell_size)
    pygame_title = f"Maze Generator - {algorithm_name}"

    import pygame
    pygame.display.set_caption(pygame_title)

    vis.animate(steps, delay_ms=delay_ms)

if __name__ == "__main__":
    main()