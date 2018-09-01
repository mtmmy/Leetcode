import unittest
import string

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # charDict = {}

        # for c in s:
        #     if c in charDict:
        #         charDict[c] += 1
        #     else:
        #         charDict[c] = 1
        
        # for i in range(len(s)):
        #     if charDict[s[i]] == 1:
        #         return i
        # return 0
        min_idx = float('inf')
        for ch in string.ascii_lowercase:
            l, r = s.find(ch), s.rfind(ch)
            if l != -1 and l == r and l < min_idx:
                min_idx = l
        return min_idx if min_idx != float('inf') else -1

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(0, target.firstUniqChar("leetcode"))
        self.assertEqual(2, target.firstUniqChar("loveleetcode"))

if __name__ == '__main__':
    unittest.main()    
        