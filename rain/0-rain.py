def rain(walls):
    """
    Calculate how much rainwater is retained between walls.

    Args:
        walls (list): A list of non-negative integers representing wall heights.

    Returns:
        int: Total amount of trapped rainwater.
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    water = 0

    # Precompute max heights from the left and right
    left_max = [walls[0]] + [0] * (n - 1)
    right_max = [0] * (n - 1) + [walls[-1]]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Accumulate trapped water
    for i in range(n):
        trapped = min(left_max[i], right_max[i]) - walls[i]
        if trapped > 0:
            water += trapped

    return water
