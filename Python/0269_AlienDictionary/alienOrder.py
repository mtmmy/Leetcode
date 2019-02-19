import unittest
from collections import deque
from collections import defaultdict

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        orderSet, letters = set([]), set([])
        indegree = defaultdict(int)
        queue, result, n = deque([]), "", len(words)
        
        for word in words:
            letters |= set(list(word))
        
        for i in range(n - 1):
            shorter, j = min(len(words[i]), len(words[i + 1])), 0
            while j < shorter:
                if words[i][j] != words[i + 1][j]:
                    # add a tuple where tuple[0] is a prior of tuple[1]
                    orderSet.add((words[i][j], words[i + 1][j]))
                    break
                j += 1
                
        for p in orderSet:
            indegree[p[1]] += 1
        
        # letters without indegrees have highest priority
        # push these letters into the queue as starter characters
        for l in letters:
            if l not in indegree:
                queue.append(l)
                result += l
                
        while queue:
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
        