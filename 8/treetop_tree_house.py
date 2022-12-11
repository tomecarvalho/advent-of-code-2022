def tree_visible(grid, row, col):
    height = grid[row][col]
    # Check left, right, up, down
    return all(grid[row][c] < height for c in range(col - 1, -1, -1)) \
        or all(grid[row][c] < height for c in range(col + 1, len(grid[row]))) \
        or all(grid[r][col] < height for r in range(row - 1, -1, -1)) \
        or all(grid[r][col] < height for r in range(row + 1, len(grid)))


def solve():
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()
        height = len(grid)
        width = len(grid[0])
        n_visible_trees = sum(tree_visible(grid, row, col)
                              for row in range(height) for col in range(width))
        print(f"Solution #1: {n_visible_trees}")


solve()
