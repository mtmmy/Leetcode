class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            result.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return result

target = Solution()
target.pancakeSort([3,2,4,1])