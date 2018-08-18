class Solution:
    result = {}
    smallest = -1
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bestSubAry = 0
        bestTwoSubAry = [0, k]
        bestThreeSubAry = [0, k, k * 2]
        
        subArySum = sum(nums[0:k])
        subAryTwoSum = sum(nums[k:k * 2])
        subAryThreeSum = sum(nums[k * 2:k * 3])
        
        bestSubArySum = subArySum
        bestTwoSubArySum = subArySum + subAryTwoSum
        bestThreeSubArySum = subArySum + subAryTwoSum + subAryThreeSum
        
        subAryIdx = 1
        subAryTwoIdx = 1 + k
        subAryThreeIdx = 1 + 2 * k
        
        
        while subAryThreeIdx <= len(nums) - k:
            subArySum = subArySum + nums[subAryIdx + k - 1] - nums[subAryIdx - 1]
            subAryTwoSum = subAryTwoSum + nums[subAryTwoIdx + k - 1] - nums[subAryTwoIdx - 1]
            subAryThreeSum = subAryThreeSum + nums[subAryThreeIdx + k - 1] - nums[subAryThreeIdx - 1]
            
            if subArySum > bestSubArySum:
                bestSubArySum = subArySum
                bestSubAry = subAryIdx
                
            if subAryTwoSum + bestSubArySum > bestTwoSubArySum:
                bestTwoSubArySum = bestSubArySum + subAryTwoSum
                bestTwoSubAry = [bestSubAry, subAryTwoIdx]
                
            if subAryThreeSum + bestTwoSubArySum > bestThreeSubArySum:
                bestThreeSubArySum = bestTwoSubArySum + subAryThreeSum
                bestThreeSubAry = bestTwoSubAry + [subAryThreeIdx]
            
            subAryIdx += 1
            subAryTwoIdx += 1
            subAryThreeIdx += 1
            
        return bestThreeSubAry
        
        