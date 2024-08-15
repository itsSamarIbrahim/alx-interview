#!/usr/bin/python3

def canUnlockAll(boxes):
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
