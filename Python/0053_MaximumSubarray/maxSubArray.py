class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            result, curMax = nums[0], nums[0]

            for num in nums[1:]:
                curMax = max(curMax + num, num)
                result = max(result, curMax)

            return result