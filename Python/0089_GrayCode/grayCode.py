class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result, v = [0], 1
        for i in range(1, n + 1):
            for x in result[::-1]:
                result.append(v + x)
            v *= 2
        return result

if __name__ == "__main__":
    target = Solution()
    target.grayCode(2)