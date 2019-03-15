class Solution:
    def shortestSuperstring(self, A: 'List[str]') -> 'str':
        n = len(A)
        distMatrix = [[0] * n for _ in range(n)]
        def calcDistance(a, b):
            for i in range(1, len(a)):
                if b.startswith(a[i:]):
                    return len(a) - i
            return 0
        
        for i in range(n):
            for j in range(n):                
                distMatrix[i][j] = calcDistance(A[i], A[j])
        
        # The problem becomes finding the shortest path that visits all nodes exactly once.
        # Brute force DFS would take O(n!) time.
        # A DP solution costs O(n^2 2^n) time.
        # 
        # Let's consider integer from 0 to 2^n - 1. 
        # Each i contains 0-n 1 bits. Hence each i selects a unique set of strings in A.
        # Let's denote set(i) => {A[j] | j-th bit of i is 1}
        # dp[i][k] => shortest superstring of set(i) ending with A[k]
        #
        # e.g. 
        #   if i = 6 i.e. 110 in binary. dp[6][k] considers superstring of A[2] and A[1].
        #   dp[6][1] => the shortest superstring of {A[2], A[1]} ending with A[1].
        #   For this simple case dp[6][1] = concatenate(A[2], A[1])

        dp = [[''] * n for _ in range(1 << n)]
        for i in range(1 << n):
            for k in range(n):
                # skip if A[k] is not in set(i) 
                if not (i & (1 << k)):
                    continue
                # if set(i) == {A[k]}
                if i == 1 << k:
                    dp[i][k] = A[k]
                    continue
                for j in range(n):
                    if j == k:
                        continue
                    if i & (1 << j):
                        # the shortest superstring if we remove A[k] from the set(i)
                        s = dp[i ^ (1 << k)][j]
                        s += A[k][distMatrix[j][k]:]
                        if dp[i][k] == '' or len(s) < len(dp[i][k]):
                            dp[i][k] = s

        min_len = float('inf')
        result = ''

        # find the shortest superstring of all candidates ending with different string
        for i in range(n):
            s = dp[(1 << n) - 1][i]
            if len(s) < min_len:
                min_len, result = len(s), s
        return result

strings = ["catg","ctaagt","gcta","ttca","atgcatc"]
target = Solution()
print(target.shortestSuperstring(strings))