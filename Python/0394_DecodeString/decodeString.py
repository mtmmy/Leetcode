import unittest

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, num = [["", 1]], ""

        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                stack.append(["", int(num)])
                num = ""
            elif ch == "]":
                string, k = stack.pop()
                stack[-1][0] += string * k
            else:
                stack[-1][0] += ch
        return stack[0][0]
            

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual("accaccacc", target.decodeString("3[a2[c]]"))

if __name__ == '__main__':
    unittest.main()
        