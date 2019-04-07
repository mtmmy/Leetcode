class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        L = list(map(int, str(N + 1)))
        res, n = 0, len(L)

        def permutation(m, n):
            ans = 1
            for num in range(m, m - n, -1):
                ans *= num
            return ans
        
        # run permutation on number 1 ~ 9
        for i in range(1, n): 
            res += 9 * permutation(9, i - 1)
            
        # e.g. N = 3045
        # N + 1 = 3046
        # first iteration of the outer loop i = 0, x = 3
        # inner loop starts from 1
        # which calculate non-repeated number between 1000 ~ 1999
        # here are three digits to compute, and we've used one digit (here is 1),
        # so the number of permutations of these three digits is P(9, 3)
        # compute the number of permutations between 2000 ~ 2999 as well
        # second iteration of the outer loop: i = 1, x = 0 then add 2 to the set
        # inner loop starts from 0 and stops immediately because x = 0 and add 0 to the set
        # 3rd iteration of the outer loop: i = 2, x = 4
        # inner loop starts from 0 to count between 0 ~ 9 and we've been use two numbers
        # so the permutations here is P(7, 1) for 0x, 1x, 2x, and 3x
        # last digits simply counts to 5
        s = set()
        for i, x in enumerate(L):
            # 0 can't be apply at the first digit
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += permutation(9 - i, n - i - 1)
            if x in s: break
            s.add(x)
            
        # all numbers minus non-repeated numbers is the answer
        return N - res