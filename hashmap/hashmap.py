import os
from lfu import LFUCache


class HashMap:
    def __init__(self, max_keys, storage="storage", eviction_policy="LFU"):
        self.lfu = LFUCache(capacity=max_keys)
        self.storage_path = os.path.join(".", storage)
        try:
            if not os.path.exists(self.storage_path):
                os.makedirs(self.storage_path)
            # create data.txt
            self.data_file = os.path.join(self.storage_path, "data.txt")
            if not os.path.exists(self.data_file):
                with open(self.data_file, 'a') as file:
                    pass

            self.data_file_write=open(self.data_file, 'a') # write handle
            self.data_file_read=open(self.data_file, 'r') # read handle
        except OSError as e:
            raise Exception(f"Failed to setup storage: {e}")


    def set(self, key, value) -> bool:
        """
        1. first write to storage disk
        2. then write to memory (LFUCache )
        3. return ack to user
        """
        try:
            data = f"{key}:{value}\n"
            self.data_file_write.write(data)
            self.data_file_write.flush() #forcing write to disk
            self.lfu.put(key, value)
            return True
        except Exception as e:
            return False

    def get(self, key):
        data = self.lfu.get(key)
        if data != -1: # LFU returns -1 when no data 
            return data # available hot

        self.data_file_read.seek(0) # reset to beginning
        for line in self.data_file_read:
            line = line.strip()
            try:
                if ":" in line:
                    _key, _value = line.split(":",1)
                    if _key.strip() == key:
                        self.lfu.put(key, _value.strip()) # put in memory
                        return _value.strip()
                else:
                    return None
            except Exception as e:
                return None
        return None
    
    def __del__(self):
        # make sure that file descriptors remain closed
        if hasattr(self, 'data_file_write'):
            self.data_file_write.close()
        if hasattr(self, 'data_file_read'):
            self.data_file_read.close()
         

if __name__  == "__main__":
    hashmap = HashMap(max_keys=3)
    
    hashmap.set("user1", "Alice")
    hashmap.set("user2", "Bob")
    hashmap.set("user3", "Charlie")

    print(hashmap.get("user1"))
    print(hashmap.get("user2"))

    hashmap.set("user4", "David")

    print(hashmap.get("user1"))
    print(hashmap.get("user2"))
    print(hashmap.get("user3"))



