import unittest

class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        
        length = len(n)
        candidates = [str(10 ** i + j) for i in (length - 1, length) for j in (-1, 1)]
        prefix = n[:(length + 1) // 2]
        prefix_int = int(prefix)
        for start in map(str, (prefix_int - 1, prefix_int, prefix_int + 1)):
            candidates.append(start + (start[:-1] if length % 2 else start)[::-1])
        
        def delta(x):
            return abs(int(n) - int(x))
        
        ans = None
        for cand in candidates:
            if cand != n and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        # self.assertEqual("-1", target.nearestPalindromic("0"))
        # self.assertEqual("0", target.nearestPalindromic("1"))
        #self.assertEqual("9", target.nearestPalindromic("10"))
        #self.assertEqual("121", target.nearestPalindromic("123"))
        #self.assertEqual("1221", target.nearestPalindromic("1234"))
        #self.assertEqual("1221", target.nearestPalindromic("1276"))
        self.assertEqual("1331", target.nearestPalindromic("12772"))

if __name__ == '__main__':
    unittest.main()
        