def tree_visible(grid, row, col):
    height = grid[row][col]
    # Check left, right, up, down
    return all(grid[row][c] < height for c in range(col - 1, -1, -1)) \
        or all(grid[row][c] < height for c in range(col + 1, len(grid[row]))) \
        or all(grid[r][col] < height for r in range(row - 1, -1, -1)) \
        or all(grid[r][col] < height for r in range(row + 1, len(grid)))


def tree_scenic_score(grid, row, col):
    height = grid[row][col]
    left, right, up, down = 0, 0, 0, 0
    for c in range(col - 1, -1, -1):
        left += 1
        if grid[row][c] >= height:
            break
    for c in range(col + 1, len(grid[row])):
        right += 1
        if grid[row][c] >= height:
            break
    for r in range(row - 1, -1, -1):
        up += 1
        if grid[r][col] >= height:
            break
    for r in range(row + 1, len(grid)):
        down += 1
        if grid[r][col] >= height:
            break
    return left * right * up * down


def solve():
    with open("input.txt", "r") as f:
        grid = [[int(c) for c in line] for line in f.read().splitlines()]
        height = len(grid)
        width = len(grid[0])
        n_visible_trees = sum(tree_visible(grid, row, col)
                              for row in range(height) for col in range(width))
        print(f"Solution #1: {n_visible_trees}")
        max_scenic_score = max(tree_scenic_score(grid, row, col)
                               for row in range(height) for col in range(width))
        print(f"Solution #2: {max_scenic_score}")


solve()
