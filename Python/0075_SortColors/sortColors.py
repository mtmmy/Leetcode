class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Solution 1:
        # count = [0, 0, 0]

        # for i in range (len(nums)):
        #     count[nums[i]] += 1

        # nums.clear()
        # for i in range (len(count)):
        #     for j in range(count[i]):
        #         nums.append(i)

        # Solution 2:
        n = len(nums) - 1
        red, blue = 0, n
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[red], nums[i] = nums[i], nums[red]
                red += 1
            elif nums[i] == 2:
                nums[blue], nums[i] = nums[i], nums[blue]
                blue -= 1
                i -= 1
            i += 1
            

if __name__ == "__main__":
    target = Solution()
    colors = [1,2,0]
    target.sortColors(colors)