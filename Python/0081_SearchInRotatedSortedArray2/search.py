class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # seems slow, but faster
        # if len(nums) == 0:
        #     return False        
        
        # if target >= nums[0]:
        #     lastN = nums[0]
        #     for n in nums:
        #         if n < lastN:
        #             return False
        #         if n == target:
        #             return True
        #         lastN = n
        # else:
        #     lastN = nums[-1]
        #     for n in reversed(nums):
        #         if n > lastN:
        #             return False
        #         if n == target:
        #             return True
        #         lastN = n
        # return False
        if len(nums) == 0:
            return False        

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False
            
            
if __name__ == "__main__":
    target = Solution()
    nums = [0, 0, 0, 0, 0, 0, 0]
    
    print(target.search(nums, 0))
    print(target.search(nums, 3))