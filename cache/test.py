import unittest
import time

from cache import Cache


class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache(2, 10)
    
    def test_basic_put_get(self):
        print("Testing for basic put and get")
        # Test Case 1: Add and retrive
        self.cache.put("key1", "value1")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, "value1")
        print("simple get and add testing done.")

        # Test Case 2: Retrive non-existent key
        # retrieve non existent key : "keyX"
        keyX_result = self.cache.get("keyX")
        self.assertEqual(keyX_result, None)
        print("non-existent key retrieval testing done")

        # Test Case 3: Update existing key
        self.cache.put("key1", "value1")
        self.cache.put("key1", "value2")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, "value2")
        print("update existing key, testing done")
        
        # Test Case 4: Remove key
        self.cache.put("key1", "value1")
        self.cache.remove("key1")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, None)
        print("remove key testing done")
    
    
        # Test Case 5: Evict on capacity
        self.cache.put("key1", "value1")
        self.cache.put("key2", "value2")
        self.cache.put("key3", "value3")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, None)
        print("evict on capacity testing done")
    
    
    def test_ttl_eviction(self):
        print("testing for TTL Eviction. Eviction time is 10 seconds. starting test for TTL.")
        self.cache.put("key1", "value1")
        print("sleeping for 5 seconds")
        time.sleep(5)
        self.cache.put("key2", "value2")
        print("sleeping for 5 seconds")
        time.sleep(5)
        print("10 seconds have passed.")
        key1_result = self.cache.get("key1")
        self.assertEqual(key1_result, None)

    def test_backing_store(self):
        print("testing backing store")
        # storing in backing store
        self.cache.backing_store.put("store_key1", "store_value1")

        # cache miss - should fetch from backing store
        print("cache miss, fetching from backing store..")
        result = self.cache.get("store_key1")
        self.assertEqual(result, "store_value1")

        #should be in cache, verify cache hit
        print("fetching same key again, should be cache hit..")
        result2 = self.cache.get("store_key1")
        self.assertEqual(result2, "store_value1")


if __name__ == "__main__":
    unittest.main()