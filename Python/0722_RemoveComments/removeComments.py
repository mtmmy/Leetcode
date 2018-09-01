import unittest

class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """

        result = []
        isBlock = 0
        out = ""

        for line in source:
            i = 0
            while i < len(line):
                if isBlock == 1:
                    if i < len(line) - 1:
                        t = line[i:i + 2]
                        if t == "*/":
                            isBlock = 0
                            i += 1
                else:
                    if i == len(line) - 1:
                        out += line[i]
                    else:
                        t = line[i:i + 2]
                        if t == "/*":
                            isBlock = 1
                            i += 1
                        elif t == "//":
                            break
                        else:
                            out += line[i]
                i += 1
            
            if len(out) != 0 and isBlock == 0:
                result.append(out)
                out = ""        
        
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        test = ["a/*comment", "line", "more_comment*/b"]
        self.assertEqual(["ab"], target.removeComments(test))
        
if __name__ == '__main__':
    unittest.main()
    