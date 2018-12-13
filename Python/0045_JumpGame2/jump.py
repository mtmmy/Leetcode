import unittest

class Solution:        
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps, curEnd, curFarthest, n = 0, 0, 0, len(nums)

        for i in range(n - 1):
            curFarthest = max(nums[i] + i, curFarthest)
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest
        return jumps

    def jump2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0

        def maxIdx(jumpRange):
            maximumIdx = 0
            maxNextIdx = 0
            for i in range(len(jumpRange)):
                if jumpRange[i] + i >= maxNextIdx:
                    maxNextIdx = jumpRange[i] + i
                    maximumIdx = i
            return maximumIdx
        
        i, n, steps = 0, len(nums), 0
        
        while i < n:
            jumpAbi = 1 if nums[i] == 0 else nums[i]
            if i + jumpAbi >= n - 1:
                steps += 1
                break
            nextMax = maxIdx(nums[i:i+jumpAbi+1])
            i += jumpAbi if nextMax == 0 else nextMax
            steps += 1
        return steps                

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(0, target.jump([0]))
        self.assertEqual(2, target.jump([2,3,1,1,4]))
        self.assertEqual(2, target.jump([2,3,5,1,4,1,1]))

if __name__ == '__main__':
    unittest.main()
        