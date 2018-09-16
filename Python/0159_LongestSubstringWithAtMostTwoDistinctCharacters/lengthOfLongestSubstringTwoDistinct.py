import unittest

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) <= 2:
            return 0 if not s else len(s)
        
        left, cur, maxLen = 0, -1, 0

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                continue
            if cur != -1 and s[right] != s[cur]:
                maxLen = max(maxLen, right - left)
                left = cur + 1
            cur = right - 1
        
        return max(maxLen, len(s) - left)    
    def lengthOfLongestSubstringTwoDistinct2(self, s):
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

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(3, target.lengthOfLongestSubstringTwoDistinct("eceba"))
        self.assertEqual(5, target.lengthOfLongestSubstringTwoDistinct("ccaabbb"))

if __name__ == '__main__':
    unittest.main()
        