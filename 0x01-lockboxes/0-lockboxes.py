#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each box may contain keys to the other
    boxes.

    Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys are positive integers
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    if not boxes:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    return len(keys) == len(boxes)
