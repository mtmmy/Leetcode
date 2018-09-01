import unittest
from collections import deque

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        orderSet = set([])
        letters = set([])
        indegree = {}
        queue = deque([])
        result = ""
        n = len(words)
        for word in words:
            letters |= set(list(word))
        
        for i in range(n - 1):
            shorter = min(len(words[i]), len(words[i + 1]))
            j = 0
            while j < shorter:
                if words[i][j] != words[i + 1][j]:
                    orderSet.add((words[i][j], words[i + 1][j]))
                    break
                j += 1
            if j == shorter and len(words[i]) > len(words[i + 1]):  #when no node has outdegrees
                return ""

        for p in orderSet:
            if p[1] in indegree:
                indegree[p[1]] += 1
            else:
                indegree[p[1]] = 1
        
        for l in letters:
            if l not in indegree or indegree[l] == 0:
                queue.append(l)
                result += l
        
        while len(queue) != 0:
            c = queue.popleft()
            for p in orderSet:
                if p[0] == c:
                    indegree[p[1]] -= 1
                    if indegree[p[1]] == 0:
                        queue.append(p[1])
                        result += p[1]
                    
        return result if len(letters) == len(result) else ""

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual("wertf", target.alienOrder(["wrt","wrf","er","ett","rftt"]))
        self.assertEqual("zx", target.alienOrder(["z", "x"]))
        self.assertEqual("", target.alienOrder(["z", "x", "z"]))
        self.assertEqual("", target.alienOrder(["wrtkj","wrt"]))

if __name__ == '__main__':
    unittest.main()
        