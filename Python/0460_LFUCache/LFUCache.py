import collections
class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = {}
        self.freq = collections.defaultdict(collections.OrderedDict)
        self.minFreq = 1
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        else:
            value, freq = self.dict[key]
            del self.freq[freq][key]
            if freq == self.minFreq and not self.freq[freq]:
                self.minFreq += 1
            self.freq[freq + 1][key] = value
            self.dict[key] = (value, freq + 1)
            return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if key in self.dict:
            old, freq = self.dict[key]
            self.dict[key] = (value, freq)
            self.get(key)
        elif len(self.dict) >= self.capacity:
            old_key, val = self.freq[self.minFreq].popitem(last=False)
            del self.dict[old_key]
            self.minFreq = 1
            self.dict[key] = (value, 1)
            self.freq[1][key] = value
        else:
            self.minFreq = 1
            self.dict[key] = (value, 1)
            self.freq[1][key] = value
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)