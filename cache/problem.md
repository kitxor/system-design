

## Design a Cache (in-memory) 

### Features:

* O(1) get and put operations
* *fixed* capacity.
* eviction policy: LRU

### Supported Operations:

*put(key, value)*

- if at capacity evict using LRU then add
- else: add to cache


*get(key):*

- if present in cache: return value
- if not present in cache: fetch from persitant store -> warm cache -> return value
- if not found in cache and persitant store -> return null

remove(key):

- remove the key-value pair 

### Configuration options

Expiration: Expire items ( remove from cache ) after the specified duration has passed since the last access
TTL resets after each `get()` and `put()` 

Maximum size: capacity

Write policy: specify the methodology used to propagate updates in cached data


-----

Design Choices:

data structure: doubly linked list + Hash Map

hash map : key to node (DLL Node), O(1) access to nodes

DLL : maintains the order in LRU
Head: most recently used
Tail : least recently used
O(1) : removal and addition
