import unittest

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        
        result = []
        for height, pos in people:
            result.insert(pos, [height, pos])
        
        return result


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]
        test = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
        self.assertEqual(expected, target.reconstructQueue(test))

if __name__ == '__main__':
    unittest.main()
        