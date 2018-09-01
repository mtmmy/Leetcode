import unittest

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([w[::-1] for w in s.split(" ")])

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", target.reverseWords("Let's take LeetCode contest"))

if __name__ == '__main__':
    unittest.main()    
        