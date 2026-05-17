import random
from grid import Grid, Cell, Edge

def prim(grid: Grid) -> list[tuple]:
    """Generates a maze using Prim's algorithm. Returns a list of steps taken, where each step is a tuple of (Edge, bool) indicating the edge added and whether it was added to the maze."""
    start = Cell(random.randint(0, grid.rows - 1), random.randint(0, grid.cols - 1))

    visited: set[Cell] = set()
    frontier: list[Edge] = []

    def add_frontier(cell: Cell) -> None:
        """Adds the neighboring edges of a cell to the frontier."""
        neighbors = [Cell(cell.row, cell.col + 1), Cell(cell.row, cell.col - 1), Cell(cell.row + 1, cell.col), Cell(cell.row - 1, cell.col)]
        
        for neighbor in neighbors:
            if 0 <= neighbor.row < grid.rows and 0 <= neighbor.col < grid.cols and neighbor not in visited:
                frontier.append(Edge(cell, neighbor))

    add_frontier(start)
    steps = []

    while frontier:
        idx = random.randint(0, len(frontier) - 1)
        edge = frontier.pop(idx)

        if edge.cell_b in visited:
            steps.append((edge, False))
            continue

        visited.add(edge.cell_b)
        steps.append((edge, True))

        add_frontier(edge.cell_b)

    return steps
