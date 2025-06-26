import unittest
from cache import Cache
import time

class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache(2, 10)
    
    def test_basic_put_get(self):
        # Test Case 1: Add and retrive
        self.cache.put("key1", "value1")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, "value1")

        # Test Case 2: Retrive non-existent key
        # retrieve non existent key : "keyX"
        keyX_result = self.cache.get("keyX")
        self.assertEqual(keyX_result, None)        

        # Test Case 3: Update existing key
        self.cache.put("key1", "value1")
        self.cache.put("key1", "value2")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, "value2")
        
        # Test Case 4: Remove key
        self.cache.put("key1", "value1")
        self.cache.remove("key1")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, None)
    
    
        # Test Case 5: Evict on capacity
        self.cache.put("key1", "value1")
        self.cache.put("key2", "value2")
        self.cache.put("key3", "value3")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, None)
    
    
    def test_ttl_eviction(self):
        print("eviction time is 10 seconds. starting test for TTL.")
        self.cache.put("key1", "value1")
        print("sleeping for 5 seconds")
        time.sleep(5)
        self.cache.put("key2", "value2")
        print("sleeping for 5 seconds")
        time.sleep(5)
        print("10 seconds have passed.")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, None)
    
if __name__ == "__main__":
    unittest.main()