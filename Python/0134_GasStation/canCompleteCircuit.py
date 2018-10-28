class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total, localSum, start = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            localSum += gas[i] - cost[i]
            if localSum < 0:
                start = i + 1
                localSum = 0
        
        return -1 if total < 0 else start
                
        
                