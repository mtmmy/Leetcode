class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            slow = nums[0]
            fast = nums[nums[0]]
            
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]                
                
            fast = 0
            
            while fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            return slow
            
        return -1

target = Solution()
target.findDuplicate([1,3,4,2,2])