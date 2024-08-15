#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be opened given
the keys contained in each box. The function uses a breadth-first search (BFS)
approach to traverse through the boxes and check if all boxes can be unlocked
starting from box 0.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened starting from box 0.

    Args:
        boxes (list of list of int): A list where each element is a list of
        integers representing the keys contained in each box. The integer
        value corresponds to the box number that can be unlocked.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    # Initialize the set of unlocked boxes and the queue for BFS
    unlocked = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        # Get the list of keys from the current box
        keys = boxes[current_box]

        for key in keys:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                queue.append(key)

    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
