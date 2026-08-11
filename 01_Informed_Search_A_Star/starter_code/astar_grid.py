"""
Assignment starter: A* search on a grid.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_astar_grid.py rely on them).

Grid legend:
    'S' = start
    'G' = goal
    '#' = wall (cannot be entered)
    '.' = free cell

Run this file directly to see your solver in action:
    python astar_grid.py
"""
import heapq

# The assignment grid. Do not edit this -- your solver must work on this
# AND on any other valid grid (the test file uses different grids too).
ASSIGNMENT_GRID = [
    "S.......",
    ".#..#.#.",
    ".#....#.",
    ".###.##.",
    "...#....",
    "##.#.##.",
    ".....#..",
    ".##...G.",
]

ROWS = len(ASSIGNMENT_GRID)
COLS = len(ASSIGNMENT_GRID[0])


def find_cell(grid, symbol):
    """Return the (row, col) of `symbol` in `grid`. Already implemented."""
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == symbol:
                return (r, c)
    raise ValueError(f"Symbol {symbol!r} not found in grid")


def is_walkable(grid, r, c):
    """Return True if (r, c) is inside the grid and not a wall.

    Already implemented -- use this inside your neighbours() function.
    """
    rows, cols = len(grid), len(grid[0])
    if not (0 <= r < rows and 0 <= c < cols):
        return False
    return grid[r][c] != "#"


def neighbours(grid, node):
    """Yield the valid 4-directional neighbours of `node` in `grid`."""
    r, c = node
    # Up, Down, Left, Right moves
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if is_walkable(grid, nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
    """Return the Manhattan distance between `node` and `goal`."""
    (r1, c1) = node
    (r2, c2) = goal
    return abs(r1 - r2) + abs(c1 - c2)


def reconstruct_path(came_from, current):
    """Rebuild the path from start to `current` using the came_from map.

    Already implemented.
    """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(grid, start, goal):
    """Implement the A* algorithm on a grid.

    Returns:
        (path, cost): path is a list of (row, col) tuples or None if no path.
                      cost is an int or float('inf') if no path.
    """
    open_heap = []
    g_score = {start: 0}
    f_start = heuristic(start, goal)

    # Priority queue entry: (f, -g, row, col, node)
    # Prefer larger g to break ties when f is equal[cite: 5, 6]
    heapq.heappush(open_heap, (f_start, -0, start[0], start[1], start))

    came_from = {}
    closed = set()

    while open_heap:
        f, neg_g, _, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue

        # Stop as soon as goal is POPPED from the priority queue[cite: 3, 6]
        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        closed.add(current)
        g = g_score[current]

        for nb in neighbours(grid, current):
            if nb in closed:
                continue

            tentative_g = g + 1  # Each move on grid costs 1[cite: 5]
            if nb not in g_score or tentative_g < g_score[nb]:
                came_from[nb] = current
                g_score[nb] = tentative_g
                f_nb = tentative_g + heuristic(nb, goal)
                heapq.heappush(
                    open_heap, (f_nb, -tentative_g, nb[0], nb[1], nb)
                )

    return None, float("inf")


if __name__ == "__main__":
    start = find_cell(ASSIGNMENT_GRID, "S")
    goal = find_cell(ASSIGNMENT_GRID, "G")
    print(f"Start: {start}, Goal: {goal}")

    path, cost = astar(ASSIGNMENT_GRID, start, goal)

    if path:
        print(f"Path found (cost={cost}):")
        print(" -> ".join(str(p) for p in path))
    else:
        print("No path exists.")
