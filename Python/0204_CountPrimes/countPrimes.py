import unittest
import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # isPrime = [True] * n
        # primes = 0
        # for i in range (2, n):
        #     if isPrime[i]:
        #         primes += 1
        #         j = 2
        #         while i * j < n:
        #             isPrime[i * j] = False
        #             j += 1
        # return primes

        if n < 2:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i:n:i] = [0] * len(primes[i * i:n:i])
        return sum(primes)

        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(4, target.countPrimes(10))

if __name__ == '__main__':
    unittest.main()    
        