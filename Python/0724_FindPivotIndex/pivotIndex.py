class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)
        
        for i in range(len(nums)):
            right -= nums[i]
            if right == left:
                return i
            left += nums[i]
        return -1