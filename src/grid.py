from dataclasses import dataclass
from typing import Iterator

@dataclass(frozen=True)
class Cell:
    row: int
    col: int

@dataclass(frozen=True)
class Edge:
    cell_a: Cell
    cell_b: Cell

class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

        self.passages: set[Edge] = set()

    def cells(self) -> Iterator[Cell]:
        for row in range(self.rows):
            for col in range(self.cols):
                yield Cell(row, col)

    def edges(self) -> Iterator[Edge]:
        """Returns all edges between adjacent cells in the grid."""
        result = []

        for cell in self.cells():
            if cell.col + 1 < self.cols:
                result.append(Edge(cell, Cell(cell.row, cell.col + 1)))

            if cell.row + 1 < self.rows:
                result.append(Edge(cell, Cell(cell.row + 1, cell.col)))

        return result
    
    def add_passage(self, edge: Edge) -> None:
        """Adds a passage between two cells in the grid."""
        self.passages.add(edge)
    
    def has_passage(self, edge: Edge) -> bool:
        """Checks if a passage exists between two cells in the grid."""
        return Edge(edge.cell_a, edge.cell_b) in self.passages or Edge(edge.cell_b, edge.cell_a) in self.passages
    
    def __repr__(self) -> str:
        return f"Grid({self.rows}x{self.cols}, {len(self.passages)} passages)"