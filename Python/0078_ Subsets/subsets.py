class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in nums:
            for j in range(len(result)):
                newset = result[j].copy()
                newset.append(i)
                result.append(newset)
        return result
if __name__ == "__main__":
    target = Solution()
    result = target.subsets([1, 2, 3, 4])