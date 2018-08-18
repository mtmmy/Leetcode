class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # for i in range(n):
        #     if nums[i] == 0:
        #         for j in range(i, n):
        #             if nums[j] != 0:
        #                 break;
        #         if j != i and j != n:
        #             nums[i], nums[j] = nums[j], nums[i]
        
        index = 0
        for i in range(n):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        
        for i in range(index, n):
            nums[i] = 0
        
                
                