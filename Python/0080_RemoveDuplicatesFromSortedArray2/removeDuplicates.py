class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i = 0
        # lastNum = 0
        # numCount = 0
        # while i < len(nums):
        #     if nums[i] != lastNum:
        #         lastNum = nums[i]
        #         numCount = 1
        #     else:
        #         numCount += 1
        #         if numCount > 2:
        #             del nums[i]
        #             i -= 1
        #     i += 1
        # return len(nums)

        if len(nums) <= 2:
            return len(nums)
        
        l, i, ptr = len(nums), 2, 2
        
        while i < l:
            if nums[i] != nums[ptr - 2]:
                nums[ptr] = nums[i]
                ptr +=1
            i += 1
        
        return ptr
            
if __name__ == "__main__":
    target = Solution()
    nums = [1,1,1,2,2,3]
    
    print(target.removeDuplicates(nums))