class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        out = []
        self.dfs(result, out, n, k, 1)
        return result
    
    def dfs (self, result, out, n, k, level):
        if len(out) == k:
            result.append(out.copy())
        for i in range (level, n + 1):
            out.append(i)
            self.dfs(result, out, n, k, i + 1)
            out.pop()

if __name__ == "__main__":
    target = Solution()
    result = target.combine(5, 3)
    