class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        lowerBound = 10 ** (N - 1)
        result = []
        def dfs(num):
            if num >= lowerBound:
                result.append(num)
            else:
                tail = num % 10
                candidate1 = tail - K
                candidate2 = tail + K
                if candidate1 >= 0 and candidate1 < 10 and candidate1 == candidate2:
                    dfs(num * 10 + candidate1)
                else:
                    if candidate1 >= 0 and candidate1 < 10:
                        dfs(num * 10 + candidate1)
                    if candidate2 >= 0 and candidate2 < 10:
                        dfs(num * 10 + candidate2)        
        
        if N == 1:
            return [i for i in range(10)]
        
        for i in range(1, 10):
            if i + K < 10 or i >= K:
                dfs(i)       
        
        return result