class UnionFind:
    def __init__(self, cells):
        self.parent: dict = {cell: cell for cell in cells}
        self.rank: dict = {cell: 0 for cell in cells}

    def find(self, cell):
        """Finds the representative of the set that the cell belongs to."""
        if self.parent[cell] != cell:
            self.parent[cell] = self.find(self.parent[cell])
        return self.parent[cell]
    
    def union(self, cell_a, cell_b) -> bool :
        """Unites the sets that cell_a and cell_b belong to. Returns True if a union was performed, False if they were already in the same set."""
        root_a = self.find(cell_a)
        root_b = self.find(cell_b)

        if root_a == root_b:
            return False
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1

        return True
