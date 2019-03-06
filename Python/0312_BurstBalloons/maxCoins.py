class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * len(nums) for _ in range(len(nums))]

        def burst(left, right):
            if left > right:
                return 0
            if dp[left][right] > 0:
                return dp[left][right]
            result = 0
            for k in range(left, right + 1):
                result = max(result, nums[left - 1] * nums[k] * nums[right + 1] + burst(left, k - 1) + burst(k + 1, right))
            dp[left][right] = result
            return result
        return burst(1, n)