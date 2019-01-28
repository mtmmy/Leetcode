import unittest
import heapq

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        sortedBuilding = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in sortedBuilding:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0] != 0:
                res.append([x, -hp[0][0]])
        return res[1:]

    def getSkylineSlow(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        
        critical = []
        
        for b in buildings:
            critical += [[b[0], b[2]], [b[1], 0]]
        
        critical = sorted(critical, key=lambda x: x[0])
        
        for l, r, h in buildings:
            for i in range(len(critical)):
                x, y = critical[i]
                if y < h and x >= l and x < r:
                    critical[i][1] = h
                    
        result = [critical[0]]
        
        for i in range(1, len(critical)):
            if critical[i][1] != critical[i - 1][1]:
                result.append(critical[i])
                
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = [[2, 10],[3, 15],[7, 12],[12, 0],[15, 10],[20, 8],[24, 0]]
        test = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
        self.assertEqual(expected, target.getSkyline(test))

if __name__ == '__main__':
    unittest.main()
        