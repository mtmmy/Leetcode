import unittest
import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # isPrime = [1] * n
        # for i in range (2, int(n ** 0.5) + 1):
        #     if isPrime[i] == 1:
        #         for j in range(i * i, n, i):
        #             isPrime[j] = 0
        # return sum(isPrime[2:])

        primes = [1] * n
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i*i:n:i] = [0] * len(primes[i * i:n:i])
        return sum(primes[2:])

        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(4, target.countPrimes(10))

if __name__ == '__main__':
    unittest.main()    
        