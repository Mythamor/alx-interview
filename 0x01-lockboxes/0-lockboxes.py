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
    unlocked_boxes = {}

    for index, box in enumerate(boxes):
        if len(box) == 0 or index == 0:
            unlocked_boxes[index] = index
        for key in box:
            if key < len(boxes) and key != index:
                unlocked_boxes[key] = key
    return len(unlocked_boxes) == n
