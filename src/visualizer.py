import pygame
from grid import Grid, Edge, Cell

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 110)
RED = (200, 50, 50)
BLUE = (50, 150, 255)
GRAY = (200, 200, 200)

class Visualizer:
    def __init__(self, grid: Grid, cell_size: int = 30):
        self.grid = grid
        self.cell_size = cell_size
        self.cols = grid.cols
        self.rows = grid.rows

        self.width = self.cols * self.cell_size
        self.height = self.rows * self.cell_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Generation")
        self.clock = pygame.time.Clock()

    def _cell_rect(self, cell: Cell) -> pygame.Rect:
        x = cell.col * self.cell_size
        y = cell.row * self.cell_size

        return pygame.Rect(x, y, self.cell_size, self.cell_size)
    
    def draw(self, active_edge: Edge | None = None, accepted: bool | None = None) -> None:
        self.screen.fill(BLACK)

        for cell in self.grid.cells():
            if active_edge is not None and cell in (active_edge.cell_a, active_edge.cell_b):
                color = GREEN if accepted else RED
            else:
                color = WHITE

            x = cell.col * self.cell_size + 2
            y = cell.row * self.cell_size + 2
            size = self.cell_size - 2

            pygame.draw.rect(self.screen, color, (x, y, size, size))

            right = Cell(cell.row, cell.col + 1)
            if cell.col + 1 < self.cols and self.grid.has_passage(Edge(cell, right)):
                pygame.draw.rect(self.screen, WHITE, (x + size, y, 2, size))

            below = Cell(cell.row + 1, cell.col)
            if cell.row + 1 < self.rows and self.grid.has_passage(Edge(cell, below)):
                pygame.draw.rect(self.screen, WHITE, (x, y + size, size, 2))

        pygame.display.flip()

    def animate(self, steps: list, delay_ms: int = 30) -> None:
        step_index = 0
        running = True
        generating = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        generating = not generating

            if generating and step_index < len(steps):
                edge, accepted = steps[step_index]

                if accepted:
                    self.grid.add_passage(edge)

                self.draw(active_edge=edge, accepted=accepted)

                step_index += 1
                pygame.time.wait(delay_ms)
            elif step_index >= len(steps):
                break;
            else: 
                self.draw()
                self.clock.tick(30)

        # pygame.quit()

    def draw_solution(self, path: list) -> None:
        """Draws the path on the screen."""
        self.draw()

        for cell in path:
            x = cell.col * self.cell_size + 2
            y = cell.row * self.cell_size + 2
            size = self.cell_size - 2

            pygame.draw.rect(self.screen, BLUE, (x, y, size, size))

        start = path[0]
        end = path[-1]

        for cell, color in ((start, GREEN), (end, RED)):
            x = cell.col * self.cell_size + 2
            y = cell.row * self.cell_size + 2
            size = self.cell_size - 2

            pygame.draw.rect(self.screen, color, (x, y, size, size))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False

            self.clock.tick(30)
