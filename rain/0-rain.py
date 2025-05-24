#!/usr/bin/python3
"""
Rainwater retention module
"""


def rain(walls):
    """
    Calculates the total amount of rainwater retained between walls.

    Arguments:
        walls (list of int): List of non-negative integers
        representing wall heights.

    Returns:
        int: Total units of retained rainwater.
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    water = 0

    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate trapped water
    for i in range(n):
        water += max(0, min(left_max[i], right_max[i]) - walls[i])

    return water
