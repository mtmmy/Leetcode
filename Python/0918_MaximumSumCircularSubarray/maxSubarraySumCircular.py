class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curMin, globalMin, curMax, globalMax, total = A[0], A[0], A[0], A[0], A[0]
        for num in A[1:]:
            curMin = min(curMin + num, num)
            globalMin = min(globalMin, curMin)
            curMax = max(curMax + num, num)
            globalMax = max(globalMax, curMax)
            total += num
        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax