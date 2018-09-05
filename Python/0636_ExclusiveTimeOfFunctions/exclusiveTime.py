import unittest

class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result = [0] * n
        stack = []
        pre_time = 0

        for log in logs:
            fn, action, time = log.split(":")
            fn, time = int(fn), int(time)

            if action == "start":
                if stack:
                    result[stack[-1]] += time - pre_time
                stack.append(fn)
                pre_time = time
            else:
                result[stack.pop()] += time - pre_time + 1
                pre_time = time + 1
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([[0,1],[1,0],[3,2],[2,4]], target.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))

if __name__ == '__main__':
    unittest.main()
        