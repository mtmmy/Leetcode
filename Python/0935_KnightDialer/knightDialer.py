class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        
        for _ in range(N - 1):
            nxt = [0] * 10
            for i in range(10):
                for j in moves[i]:
                    nxt[j] += dp[i]
            dp = nxt
        
        return sum(dp) % (10 ** 9 + 7)
    

target = Solution()
print(target.knightDialer(3))