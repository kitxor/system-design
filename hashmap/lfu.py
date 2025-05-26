from collections import OrderedDict, defaultdict
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

    
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = dict()
        self.freq_to_node = defaultdict(OrderedDict)

    def put(self, key:int, value: int):
        if self.capacity == 0:
            return 

        # new key but cache is full
        if key not in self.key_to_node and len(self.key_to_node) == self.capacity:
            evicted_key, evicted_node = self.freq_to_node[self.min_freq].popitem(last=False)
            del self.key_to_node[evicted_key]

            new_node = Node(key, value) # create a new node
            self.key_to_node[key] = new_node # update  key_to_node
            self.freq_to_node[new_node.freq][key] = new_node
            self.min_freq = 1


        # new key and cache has space
        elif key not in self.key_to_node:
            node = Node(key, value)
            self.key_to_node[key] = node
            self.freq_to_node[node.freq][key] = node
            self.min_freq = 1
        
        # existing key 
        else:
            node = self.key_to_node.get(key) 
            node.value = value 
            del self.freq_to_node[node.freq][key]
            if not self.freq_to_node[node.freq] and node.freq == self.min_freq:
                self.min_freq += 1
            node.freq += 1
            self.freq_to_node[node.freq][key] = node


    def get(self, key):
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node.get(key)
        del self.freq_to_node[node.freq][key]
        if not self.freq_to_node[node.freq] and node.freq == self.min_freq:
            self.min_freq += 1
        node.freq += 1
        self.freq_to_node[node.freq][key] = node
        return node.value


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1,10)
    lfu.put(2,20)
    lfu.get(1)

    lfu.put(3,30)

    print(lfu.get(1))
    print(lfu.get(2))
    print(lfu.get(3))

    
