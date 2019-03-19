from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dest = defaultdict(list)
        for f, t in sorted(tickets)[::-1]:
            dest[f].append(t)
        route = []
        def dfs(airport):
            while dest[airport]:
                dfs(dest[airport].pop())
            route.append(airport)            
        dfs("JFK")
        return route[::-1]

target = Solution()
target.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])