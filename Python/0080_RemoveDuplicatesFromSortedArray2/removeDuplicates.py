class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        lastNum = 0
        numCount = 0
        while i < len(nums):
            if nums[i] != lastNum:
                lastNum = nums[i]
                numCount = 1
            else:
                numCount += 1
                if numCount > 2:
                    del nums[i]
                    i -= 1
            i += 1
        return len(nums)
            
if __name__ == "__main__":
    target = Solution()
    nums = [1,1,1,2,2,3]
    
    print(target.removeDuplicates(nums))