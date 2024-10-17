#!/usr/bin/python3
"""
Module to check if the boxes can be unlocked
"""


def canUnlockAll(boxes: list) -> bool:
    """
    This is a python function that traverses through a list or list of lists
    and checks if the boxes can be unlocked with the given keys
    found in other boxes
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    can_open = [False] * n  # Track which boxes can be opened
    can_open[0] = True  # The first box is unlocked
    keys = [0]  # Start with the first box

    while keys:
        current_box = keys.pop()  # Get the current box to explore

        for key in boxes[current_box]:
            if key < n and not can_open[key]:  # Check key is valid box locked
                can_open[key] = True  # Unlock the box
                keys.append(key)  # Add the key to list to explore keys later

    return all(can_open)  # Check if all boxes can be opened
