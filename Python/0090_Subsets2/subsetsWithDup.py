class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        nums.sort()
        result = [[]]
        last = nums[0]
        size = len(result)
        for i in nums:
            if i != last:
                last = i
                size = len(result)
            newSize = len(result)
            for j in range(newSize - size, len(result)):
                newset = result[j].copy()
                newset.append(i)
                result.append(newset)
            last = i
        return result
if __name__ == "__main__":
    target = Solution()
    result = target.subsetsWithDup([2, 1, 2, 2])