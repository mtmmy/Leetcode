class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n < 5:
            return count
        while n >= 5:
            n //= 5
            count += n
        return count
        

if __name__ == "__main__":
    target = Solution()
    result = target.trailingZeroes(125)
    print(result)