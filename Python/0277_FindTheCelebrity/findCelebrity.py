import unittest

class Solution:
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        def knows(a, b):
            """
            Fake API. It doesn't work
            """
            return False

        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        
        for i in range(candidate):
            if knows(candidate, i):
                return -1
            
        if i in range(n):
            if not knows(i, candidate):
                return -1
        
        return candidate
        