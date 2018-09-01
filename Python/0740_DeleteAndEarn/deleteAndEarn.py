class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        sums = { i:0 for i in range(min(nums), max(nums) + 1) }
        for num in nums:
            sums[num] += num
            
#         takePre, skipPre = 0, 0
#         for key, val in sums.items():
#             takeThis = skipPre + val
#             skipThis = max(takePre, skipPre)
#             takePre, skipPre = takeThis, skipThis
            
#         return max(takePre, skipPre)

        # solution 2
        now, last = 0, 0
        for key, val in sums.items():
            new = val + last
            if new > now:
                now, last = new, now
            else:
                last = now
        return now