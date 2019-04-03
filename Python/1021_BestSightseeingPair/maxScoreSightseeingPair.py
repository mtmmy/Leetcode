from typing import List
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n, result, cur = len(A), float('-inf'), float('-inf')
        for i in range(n):
            result = max(result, A[i] - i + cur)
            cur = max(cur, A[i] + i)
        return result