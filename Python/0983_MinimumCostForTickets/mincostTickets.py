class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        
        minCosts = [0] * 366
        travDay = [False] * 366
        
        for d in days:
            travDay[d] = True
            
        for i in range(1, 366):
            if not travDay[i]:
                minCosts[i] = minCosts[i - 1]
            else:
                minCosts[i] = min(minCosts[i - 1] + costs[0], minCosts[max(0, i - 7)] + costs[1], minCosts[max(0, i - 30)] + costs[2])
            
        return minCosts[-1]