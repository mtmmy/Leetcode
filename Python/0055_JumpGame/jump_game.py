class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        # while i < len(nums):
        #     if nums[i] >= len(nums) - i - 1:
        #         return True
        #     if nums[i] == 0:
        #         j = i
        #         while j >= 0:
        #             if nums[j] > i - j:
        #                 break
        #             j -= 1
        #         if j < 0:
        #             return False
        #         i += 1
        #     else:
        #         i += nums[i]
        # return i >= len(nums)
        reach = 0
        while i < len(nums) and i <= reach:
            reach = max(nums[i] + i, reach)
            i += 1
        return reach >= len(nums) - 1


if __name__ == "__main__":
    target = Solution()
    print(target.canJump([2, 5, 0, 0]))