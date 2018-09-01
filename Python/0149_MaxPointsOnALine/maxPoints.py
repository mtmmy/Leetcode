import unittest

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        result, n = 0, len(points)
        for i in range(n):
            dic = {}
            duplicate = 1
            for j in range(i + 1, n):
                ix, jx, iy, jy = points[i].x, points[j].x, points[i].y, points[j].y
                if ix == jx and iy == jy:
                    duplicate += 1
                    continue
                dx = jx - ix
                dy = jy - iy
                d = self.gcd(dx, dy)
                tupleD = (dx // d, dy // d)
                if tupleD in dic:
                    dic[tupleD] += 1
                else:
                    dic[tupleD] = 1
            result = max(result, duplicate)
            for key, val in dic.items():
                result = max(result, val + duplicate)
        return result

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        #self.assertEqual(3, target.maxPoints([Point(1, 1), Point(2, 2), Point(3, 3)]))
        self.assertEqual(4, target.maxPoints([Point(1,1), Point(3,2), Point(5,3), Point(4,1), Point(2,3), Point(1,4)]))

if __name__ == '__main__':
    unittest.main()    
        