import numpy as np
import time
import os

def initialize_grid(rows, cols, density=0.2):
    """Initialize the grid with random live cells."""
    return np.random.choice([0, 1], size=(rows, cols), p=[1-density, density])

def display_grid(grid):
    """Display the grid in console."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    for row in grid:
        print("".join("#" if cell else " " for cell in row))
    

def count_neighbors(grid, x, y):
    """Count live neighbors around a cell."""
    rows, cols = grid.shape
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),         (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            count += grid[nx, ny]
    return count

def update_grid(grid):
    """Compute the next generation of the grid."""
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y)
            if grid[x, y] == 1 and neighbors in [2, 3]:
                new_grid[x, y] = 1  # Stay alive
            elif grid[x, y] == 0 and neighbors == 3:
                new_grid[x, y] = 1  # Become alive
    return new_grid

def game_of_life(rows=20, cols=40, generations=50, delay=0.1):
    """Run the Game of Life simulation."""
    grid = initialize_grid(rows, cols)
    for _ in range(generations):
        display_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

if __name__ == "__main__":
    game_of_life()
