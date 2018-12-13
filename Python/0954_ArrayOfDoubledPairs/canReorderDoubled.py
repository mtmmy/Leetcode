import collections
class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return True
        
        counter = collections.Counter(A)        
        if 0 in counter and counter[0] % 2 != 0:
            return False
        
        keys = sorted(counter.keys(), key = lambda x: abs(x))
        
        for k in keys:
            if not counter[k]:
                continue
            twice = k * 2
            if not twice in counter or counter[k] > counter[twice]:
                return False
            counter[twice] -= counter[k]                
        return True
