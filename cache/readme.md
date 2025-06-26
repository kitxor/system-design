## Design a Cache (in-memory) 

----

### Design Choices:

- LRU eviction using Hash Map and doubly linked list for O(1) operations
- cache-aside for read operations (cache miss -> fetch from backing store)
- write-through policy for write operations, update both cache and backing store
- single lock for thread safety (simplicity over performance)
- access-based TTL expiration with timestamp renewal on `get/put`


### Architecture: 
- data structures: doubly linked list + Hash Map
- Hash Map for key to node mapping with O(1) access
- DLL for maintaining node ordering with O(1) add/remove operations
- `BackingStore` interface for persistent storage simulation (cache-aside)

### Bonus features implemented
- synchronous backing store loading (cache miss -> fetch from persistent storage)

### Future Scope
- Read/Write locks for better performance
- Background TTL cleanup thread
- Multiple eviction policies (LFU, FIFO)
- Refresh strategies

### Running tests
```python test.py```
