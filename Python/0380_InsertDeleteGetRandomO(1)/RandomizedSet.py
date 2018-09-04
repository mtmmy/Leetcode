import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dataSet = {}
        self.dataList = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dataSet:
            self.dataList.append(val)
            self.dataSet[val] = len(self.dataList) - 1            
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dataSet:
            target, last = self.dataSet[val], self.dataList[-1]
            self.dataList[target] = last
            self.dataList.pop()
            self.dataSet[last] = target
            del self.dataSet[val]
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.dataList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()