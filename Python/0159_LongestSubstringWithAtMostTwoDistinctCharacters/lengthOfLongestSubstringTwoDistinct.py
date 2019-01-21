import unittest

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        twoChars, i, j, n, maxLength, counter = set(), 0, 0, len(s), 0, 0

        while j < n:
            if len(twoChars) == 2 and s[j] not in twoChars:
                twoChars.clear()
                twoChars.add(s[i])
                twoChars.add(s[j])
                maxLength = max(maxLength, counter)
                counter = j - i         
            if j > 0 and s[j] != s[j - 1]:
                i = j
            if len(twoChars) < 2:
                twoChars.add(s[j])
                j += 1
                counter += 1
            elif s[j] in twoChars:
                counter += 1
                j += 1
        
        return max(maxLength, counter)
    
    def lengthOfLongestSubstringTwoDistinct2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) <= 2:
            return len(s)
        
        # fstHead: head of the first kind of character
        # fstTail: tail of the first kind of character
        fstHead, fstTail, maxLen = 0, -1, 0

        # tracker: to track the change of characters
        for tracker in range(1, len(s)):
            if s[tracker] == s[tracker - 1]:
                continue
            if fstTail != -1 and s[tracker] != s[fstTail]:
                maxLen = max(maxLen, tracker - fstHead)
                fstHead = fstTail + 1
            fstTail = tracker - 1
        
        return max(maxLen, len(s) - fstHead)

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(3, target.lengthOfLongestSubstringTwoDistinct("eceba"))
        self.assertEqual(5, target.lengthOfLongestSubstringTwoDistinct("ccaabbb"))

if __name__ == '__main__':
    unittest.main()
        