from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end to mark it as most recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if key in self.cache:
            # Move the existing key to the end to mark it as most recently used
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used item (first item in the OrderedDict)
            self.cache.popitem(last=False)
        self.cache[key] = value

    def print_cache(self):
        for key, value in self.cache.items():
            print(f"{key}: {value}")


cache = LRUCache(3)
cache.put("key1", "value1")
cache.put("key2", "value2")
cache.put("key3", "value3")
cache.print_cache()  # Output: key1: value1, key2: value2, key3: value3

print("1")

cache.get("key2")
cache.print_cache()  # Output: key1: value1, key3: value3, key2: value2 (key2 moved to the end)
print("2")

cache.put("key4", "value4")  # key1 is removed since it was the least recently used
cache.print_cache()  # Output: key3: value3, key2: value2, key4: value4
