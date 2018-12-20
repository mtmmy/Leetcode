class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        out = []

        def dfs (n, level):
            if len(out) == k:
                result.append(out[:])
            for i in range (level, n + 1):
                out.append(i)
                dfs(n, i + 1)
                out.pop()
                
        dfs(n, 1)
        return result

if __name__ == "__main__":
    target = Solution()
    result = target.combine(5, 3)
    