#!/usr/bin/python3

"""
mudule: 0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    method that uses a set to keep track of unlocked boxes
    a list to store the available keys.
    """

    # Number of boxes
    n = len(boxes)

    # Initialize a set with the first box, that's always unlocked
    unlocked_boxes = {0}

    visited_boxes = set()

    # Create a list of the keys in the first box
    keys_to_try = boxes[0]

    while keys_to_try:
        key = keys_to_try.pop()
        if key not in visited_boxes:
            visited_boxes.add(key)
            unlocked_boxes.add(key)
            keys_to_try.extend(boxes[key])

    return len(unlocked_boxes) == n
