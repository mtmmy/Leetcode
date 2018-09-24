class Solution(object):
    def changeTE(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        combinations = 0
        def search(amount, remainCoins, curComb):
            total = 0 
            if amount == 0:
                return 1
            for i in range(len(remainCoins)):
                c = remainCoins[i]
                if amount >= c:
                    combs.append(c)
                    total += search(amount - c, remainCoins[i:], combs[:])
                    combs.pop()
            return total
        
        combs = []
        for i in range(len(coins)):
            c = coins[i]
            if amount >= c:
                combs.append(c)
                combinations += search(amount - c, coins[i:], combs[:])
                combs.pop()
                
        return combinations
                
        