from dll import DLL
from node import Node
import time

from backing_store import BackingStore


class Cache:
    def __init__(self, capacity, ttl_seconds):
        self.hashmap = dict()
        self.dll = DLL()
        self.capacity = capacity
        self.ttl_seconds = ttl_seconds
        self.backing_store = BackingStore()
    
    
    
    def get(self, key,):
        """
            found in cache
            lookup in self.hashmap, get node
            move the node to front in dll (most recenlty used)
            
            not found in cache
            hit the peristant storage -> warm cache -> return to client
            
            not found in both cache and peristant storage -> return None
        """

        node = self.hashmap.get(key)
        if not node:
            # not found in-memory, call persistent storage
            # node = fetchFromPersistantStore(key)
            value = self.backing_store.get(key)
            if not value:
                return
            # warm cache, let put() handle it.
            self.put(key, value)
            return value

        # TTL logic
        time_since_last_access = time.time() - node.last_access_time
        if time_since_last_access > self.ttl_seconds: #expired 
            # delete key
            del self.hashmap[key]
            # remove node
            self.dll.remove_node(node)
            # check if backing store has the data
            value = self.backing_store.get(key)
            if not value: # not present in backing store as well
                return
            self.put(key, value) # if present in backing store -> warm cache
            return value

                    
        # delete the node and add it to the start of dll (moving to front)
        self.dll.remove_node(node)
        self.dll.add_to_front(node)    
        # update access time for TTL 
        node.last_access_time = time.time()
        
        return node.val
    
    def put(self, key, value):
        """
        create Node, add key, node pair to hashmap
        add the new node to the front
        """

        if len(self.hashmap) == self.capacity and key not in self.hashmap: #new key incrseases size, existing doesn't
            # time to evict
            # remove tail (LRU)
            lru_node = self.dll.remove_from_tail()
            # remove key from hashmap
            del self.hashmap[lru_node.key]

        # within capacity or key exists or both

        node = self.hashmap.get(key)

        # duplication of code for better readability
        # if node exists; remove it and move to front and update hashmap
        if node:
            self.dll.remove_node(node)
            new_node = Node(key, value)
            self.hashmap[key] = new_node #overwrite (no impact on capacity)
            self.dll.add_to_front(new_node) #it's a fresh node, add it
            # TTL is handed during node creation
            
        # if node does not exist create a new node and add to front, and update hashmap                
        else:
            new_node = Node(key, value)
            self.hashmap[key] = new_node #overwrite (no impact on capacity)
            self.dll.add_to_front(new_node) #it's a fresh node, add it
            # TTL is handed during node creation    
        
        
    def remove(self, key):
        """
            remove key from hash map
            remove node from dll
        """
        node = self.hashmap.get(key)
        if not node: # nothing to delete
            return 
        
        del self.hashmap[key]
        self.dll.remove_node(node)