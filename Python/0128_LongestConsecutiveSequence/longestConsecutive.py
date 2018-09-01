import unittest

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set()
        result = 0
        for num in nums:
            numSet.add(num)
        
        for num in nums:
            preNum = num - 1
            nexNum = num + 1
            if num not in numSet:
                continue
            numSet.remove(num)
            while preNum in numSet:
                numSet.remove(preNum)
                preNum -= 1
            while nexNum in numSet:
                numSet.remove(nexNum)
                nexNum += 1
            result = max(result, nexNum - preNum - 1)
        return result


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(4, target.longestConsecutive([100, 4, 200, 1, 3, 2]))
        self.assertEqual(12, target.longestConsecutive([100, 4, 200, 1, 3, 2, 6, 5, 0, 7, 9, 11, 8, 10]))
        
if __name__ == '__main__':
    unittest.main()
        