#!/usr/bin/python3
"""
0-island_perimeter.py

This module contains the function `island_perimeter` that calculates the
perimeter of an island in a 2D grid.
The grid is represented as a list of lists where:
- 0 represents water
- 1 represents land

The function returns the perimeter of the island by checking each land cell
and its neighboring cells to determine how many sides contribute to the
perimeter.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    The grid is a list of list of integers, where:
    - 0 represents water
    - 1 represents land
    Each cell is square, with a side length of 1. Cells are connected
    horizontally/vertically (not diagonally). The grid is rectangular,
    and the island is surrounded by water with no lakes (water inside
    the island).

    Parameters:
    grid (list of lists): A 2D grid (list of lists) containing 0s and 1s
      representing water and land.

    Returns:
    int: The perimeter of the island.

    Example:
    >>> grid = [
    ...     [0, 1, 0, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 1, 0, 0],
    ...     [1, 1, 0, 0]
    ... ]
    >>> island_perimeter(grid)
    12
    """

    perimeter = 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over every cell in the grid
    for row in range(rows):
        for col in range(cols):
            # If the cell is land
            if grid[row][col] == 1:
                # Check top (out of bounds means it's the edge of the grid)
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check right
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
