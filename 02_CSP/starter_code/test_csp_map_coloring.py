"""
Tests for csp_map_coloring.py

Run with:
    pytest 02_CSP/starter_code/test_csp_map_coloring.py -v
"""
import pytest
from csp_map_coloring import backtracking_search, is_consistent, VARIABLES, NEIGHBOURS, DOMAIN


def _is_valid_solution(solution, variables, neighbours):
    """Helper: check a solution assigns every variable and breaks no
    adjacency constraint.
    """
    if solution is None:
        return False
    if set(solution.keys()) != set(variables):
        return False
    for var, value in solution.items():
        for neighbour in neighbours[var]:
            if neighbour in solution and solution[neighbour] == value:
                return False
    return True


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify. Use this as your template.
# Category: typical/normal small solvable case[cite: 8]
# ---------------------------------------------------------------------
def test_given_example():
    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)


# ---------------------------------------------------------------------
# Test Case 1
# Category: Solvability -> Unsolvable / Over-constrained case[cite: 8]
# Why chosen: Tests that backtracking_search correctly fails and returns
# None when only 2 colours are provided for Australia (which requires 3)[cite: 7, 8, 11].
# ---------------------------------------------------------------------
def test_case_1():
    limited_domain = ["Red", "Green"]
    solution = backtracking_search(VARIABLES, limited_domain)
    assert solution is None


# ---------------------------------------------------------------------
# Test Case 2
# Category: Boundary / Domain case (Oversized domain with excess choices)
# Why chosen: Verifies that backtracking search smoothly finds a valid solution
# when given more colors than strictly needed (e.g., 5 colors instead of 3).
# ---------------------------------------------------------------------
def test_case_2():
    large_domain = ["Red", "Green", "Blue", "Yellow", "Purple"]
    solution = backtracking_search(VARIABLES, large_domain)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)


# ---------------------------------------------------------------------
# Test Case 3
# Category: Consistency -> Directly checking constraint logic[cite: 7, 8]
# Why chosen: Ensures is_consistent accurately flags conflicts for
# adjacent regions while permitting valid colourings[cite: 7, 9].
# ---------------------------------------------------------------------
def test_case_3():
    assignment = {"WA": "Red"}
    # NT borders WA, assigning Red must fail[cite: 9]
    assert not is_consistent(assignment, "NT", "Red")
    # Assigning Green must pass[cite: 9]
    assert is_consistent(assignment, "NT", "Green")


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))