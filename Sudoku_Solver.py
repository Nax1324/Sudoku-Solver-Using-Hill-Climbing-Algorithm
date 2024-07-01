import random

def print_grid(grid):
    for row in grid:
        print("[" + ", ".join(map(str, row)) + "]")

def find_empty_cell(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
    return None

def count_conflicts(grid, row, col, num):
    conflicts = 0
    # Check row
    for i in range(len(grid)):
        if grid[i][col] == num:
            conflicts += 1
    # Check column
    for j in range(len(grid[0])):
        if grid[row][j] == num:
            conflicts += 1
    # Check box
    box_row = row // 2
    box_col = col // 2
    for i in range(box_row * 2, box_row * 2 + 2):
        for j in range(box_col * 2, box_col * 2 + 2):
            if grid[i][j] == num:
                conflicts += 1
    return conflicts

def hill_climbing(grid):
    while True:
        empty_cell = find_empty_cell(grid)
        if not empty_cell:
            print("Puzzle Solved!")
            print_grid(grid)
            break
        row, col = empty_cell
        min_conflicts = float('inf')
        best_num = None
        for num in range(1, 5):
            conflicts = count_conflicts(grid, row, col, num)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_num = num
        grid[row][col] = best_num
        print(f"Placing value {best_num} at ({row}, {col}) with {min_conflicts} conflicts:")
        print_grid(grid)

if __name__ == "__main__":
    initial_puzzle = [
        [1, 0, 0, 4],
        [0, 0, 0, 0],
        [0, 3, 2, 0],
        [0, 0, 0, 0]
    ]
    print("Initial Puzzle:")
    print_grid(initial_puzzle)
    print()
    hill_climbing(initial_puzzle)