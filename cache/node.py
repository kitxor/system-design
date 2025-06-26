import time

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 
        # node should manage it's own metadata. caller doesn't need to worry about timestamps, maintains consistency
        self.last_access_time = time.time() # in-memory, non-distributed system 