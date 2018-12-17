class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        reach = 0
        while i < len(nums) and i <= reach:
            reach = max(nums[i] + i, reach)
            i += 1
        return reach >= len(nums) - 1


if __name__ == "__main__":
    target = Solution()
    print(target.canJump([2, 5, 0, 0]))