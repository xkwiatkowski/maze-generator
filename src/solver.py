from collections import deque
from grid import Grid, Cell, Edge

def bfs(grid: Grid, start: Cell, end: Cell) -> list[Cell] | None:
    """BFS solver - finds the shortest path between two cells in the grid. Returns a list of cells representing the path, or None if no path exists."""
    queue = deque([start])
    visited = {start}
    parent: dict[Cell, Cell | None] = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            path = []
            node: Cell | None = end

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            return path
        
        neighbors = [Cell(current.row, current.col + 1), Cell(current.row, current.col - 1), Cell(current.row + 1, current.col), Cell(current.row - 1, current.col)]

        for neighbor in neighbors:
            if 0 <= neighbor.row < grid.rows and 0 <= neighbor.col < grid.cols and neighbor not in visited and grid.has_passage(Edge(current, neighbor)):
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None
