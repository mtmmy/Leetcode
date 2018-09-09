import unittest

class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        contentMap = {}

        for s in paths:
            block = s.split(" ")
            path = block[0]
            for f in block[1:]:
                name, content = f.split("(")
                filePath = path + "/" + name

                if content not in contentMap:
                    contentMap[content] = [filePath]
                else:
                    contentMap[content].append(filePath)
        
        return [files for files in contentMap.values() if len(files) > 1]
            

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = [["root/a/1.txt","root/c/3.txt"],["root/a/2.txt","root/c/d/4.txt","root/4.txt"]]
        test = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
        self.assertEqual(expected, target.findDuplicate(test))

if __name__ == '__main__':
    unittest.main()
        