import numpy as np
from numba import njit
import time

@njit
def game_of_life_step(grid):
    n, m = grid.shape
    new_grid = np.zeros((n, m), dtype=np.int8)
    for i in range(n):
        for j in range(m):
            # считаем соседей с учётом границ (тороидальная вселенная)
            total = (grid[(i-1) % n, (j-1) % m] + grid[(i-1) % n, j] + grid[(i-1) % n, (j+1) % m] +
                     grid[i, (j-1) % m]                     + grid[i, (j+1) % m] +
                     grid[(i+1) % n, (j-1) % m] + grid[(i+1) % n, j] + grid[(i+1) % n, (j+1) % m])
            if grid[i, j] == 1:
                new_grid[i, j] = 1 if total in (2, 3) else 0
            else:
                new_grid[i, j] = 1 if total == 3 else 0
    return new_grid

# Тест скорости
size = 200
grid = np.random.randint(0, 2, (size, size), dtype=np.int8)

start = time.time()
for _ in range(100):
    grid = game_of_life_step(grid)
print(f"Numba Game of Life: {time.time() - start:.3f} сек")