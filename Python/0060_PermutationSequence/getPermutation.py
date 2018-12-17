class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result, nums, factorial = "", "123456789", [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        k -= 1
        
        print(factorial)
        for i in range(n, 0, -1):
            pos = k // factorial[i - 1]
            result += nums[pos]
            k %= factorial[i - 1]
            nums = nums[:pos] + nums[pos + 1:]
        
        return result