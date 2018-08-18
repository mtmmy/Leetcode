class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n < 2:
            return
        
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.reverse()
            return
            
        j = n - 1
        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1        

        nums[j], nums[i - 1] = nums[i - 1], nums[j]
        nums[i:] = nums[i:][::-1]     
        