class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, blue = 0, len(nums) - 1
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