class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         nums.sort()        
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return nums[i]            
#         return -1

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