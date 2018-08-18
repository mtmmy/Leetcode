import collections

class LRUCache:
        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.used = 0
        

    def get(self, key):        
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]
            
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if self.used < self.capacity:
                self.used += 1
            else:
                self.cache.popitem(last = False)
            self.cache[key] = value

if __name__ == "__main__":
    target = LRUCache(3)
    print(target.get(1))
    target.put(1, 1)
    print(target.get(1))