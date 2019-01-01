class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        result, last = [[]], nums[0]
        size = len(result)
        
        for num in nums:
            if num != last:
                last = num
                size = len(result)
            newSize = len(result)
            for j in range(newSize - size, len(result)):
                newset = result[j].copy()
                newset.append(num)
                result.append(newset)
            last = num
        return result
if __name__ == "__main__":
    target = Solution()
    result = target.subsetsWithDup([2, 1, 2, 2])