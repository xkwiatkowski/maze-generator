import random
from grid import Grid
from union_find import UnionFind

def kruskal(grid: Grid) -> list[tuple]:
    """Implements Randomized Kruskal's algorithm. Returns a list of steps taken, where each step is a tuple of the edge and whether it was accepted or not."""
    edges = grid.edges()
    random.shuffle(edges)

    uf = UnionFind(list(grid.cells()))
    steps = []

    for edge in edges:
        accepted = uf.union(edge.cell_a, edge.cell_b)
        
        steps.append((edge, accepted))

    return steps
