import unittest

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        # result, left, right, n = 20001, 0, k + 1, len(flowers)
        # days = [0] * n

        # for i in range(n):
        #     days[flowers[i] - 1] = i + 1

        # i = 0
        # while right < n:
        #     if days[i] < days[left] or days[i] <= days[right]:
        #         if i == right:
        #             result = min(result, max(days[left], days[right]))
        #         left = i
        #         right = k + i + 1
        #     i += 1 

        # return -1 if result == 20001 else result
        garden = [[i - 1, i + 1] for i in range(len(flowers))]
        garden[0][0], garden[-1][1] = None, None
        ans = -1
        for i in range(len(flowers) - 1, -1, -1):
            cur = flowers[i] - 1
            left, right = garden[cur]
            if right != None and right - cur == k + 1:
                ans = i + 1
            if left != None and cur - left == k + 1:
                ans = i + 1
            if right != None:
                garden[right][0] = left
            if left != None:
                garden[left][1] = right
        return ans

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(2, target.kEmptySlots([1,3,2], 1))
        self.assertEqual(-1, target.kEmptySlots([1,2,3], 1))

if __name__ == '__main__':
    unittest.main()