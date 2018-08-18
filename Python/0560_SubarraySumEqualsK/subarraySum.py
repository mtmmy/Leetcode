class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum = {0: 1}
        curSum = 0
        result = 0
        
        for n in nums:
            curSum += n
            if (curSum - k) in preSum:
                result += preSum[curSum - k]
            
            if curSum in preSum:
                preSum[curSum] += 1
            else:
                preSum[curSum] = 1
                
        return result