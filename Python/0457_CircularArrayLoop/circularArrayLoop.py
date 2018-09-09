import unittest

class Solution:
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapping, n = {}, len(nums)
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue
            cur = i
            while 1:
                visited[cur] = True
                next = (cur + nums[cur]) % n
                if next < 0:
                    next += n
                if next == cur or nums[next] * nums[cur] < 0:
                    break
                if next in mapping:
                    return True
                mapping[cur] = next
                cur = next
        return False


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = True
        test = [2, -1, 1, 2, 2]
        self.assertEqual(expected, target.circularArrayLoop(test))
        expected = False
        test = [-1, 2]
        self.assertEqual(expected, target.circularArrayLoop(test))

if __name__ == '__main__':
    unittest.main()
        