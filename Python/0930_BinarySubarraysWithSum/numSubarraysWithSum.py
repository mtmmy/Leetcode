import collections
class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        prefixCounter = collections.Counter({0: 1})
        prefixSum = result = 0
        for num in A:
            prefixSum += num
            result += prefixCounter[prefixSum - S]
            prefixCounter[prefixSum] += 1        
        return result