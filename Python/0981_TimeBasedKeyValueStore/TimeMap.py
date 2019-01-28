import collections

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(dict)
        

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key not in self.map:
            self.map[key][timestamp] = value
        else:
            maxK = max([k for k in self.map[key].keys()])
            if self.map[key][maxK] != value:
                self.map[key][timestamp] = value
        

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key in self.map:
            if timestamp in self.map[key]:
                return self.map[key][timestamp]
            elif self.map[key]:
                s = max([k for k in self.map[key].keys() if k < timestamp] + [-1])
                if s > -1:
                    return self.map[key][s]
                else:
                    return ""
        return ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)