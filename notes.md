# Assignment Notes

## 1. A* Heuristic Admissibility
The Manhattan distance $h(n) = |r_1 - r_2| + |c_1 - c_2|$ is admissible for 4-directional grid movement because it calculates the minimum number of orthogonal steps required to reach the goal on an ideal grid without obstacles. In any real grid, obstacles can only increase or equal the required number of steps, but never decrease it. Therefore, $h(n) \le h^*(n)$ holds for all nodes $n$, ensuring that the heuristic never overestimates the true remaining path cost and guarantees an optimal path.

## 2. Test Case Coverage Analysis

### A* Search Test Cases (`test_astar_grid.py`)
- **Given Example (Typical / Solvable)**: Open $3 \times 3$ grid without obstacles. Validates baseline shortest-path finding and path cost calculation.
- **Test Case 1 (Unsolvable / Complete Blockade)**: Edge/Stress case where walls completely seal off the goal cell. Verifies that $A^*$ handles an empty open list gracefully and returns `(None, inf)`.
- **Test Case 2 (Minimal / Boundary)**: Minimal $1 \times 2$ grid with Start and Goal directly adjacent. Confirms correct behavior on 1-step boundary paths.
- **Test Case 3 (Obstacle / Forced Detour)**: Topology case with a central wall blocking the direct path. Tests heuristic behavior and node expansion when forced to make a U-turn around obstacles.

### CSP Map Coloring Test Cases (`test_csp_map_coloring.py`)
- **Given Example (Typical / Solvable)**: Australia map using 3 colors. Verifies full backtracking search and adjacency constraint satisfaction.
- **Test Case 1 (Unsolvable / Over-constrained)**: Australia map provided with only 2 colors (since 3 are required). Confirms that `backtracking_search` correctly detects impossibility, exhausts branches, and returns `None`.
- **Test Case 2 (Oversized Domain)**: Domain boundary case providing 5 colors. Verifies that search handles extra choices cleanly without crashing or entering infinite loops.
- **Test Case 3 (Constraint Logic Check)**: Direct evaluation of `is_consistent()`. Confirms immediate detection of color collisions among adjacent regions while permitting legal assignments.