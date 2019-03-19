from typing import List
from collections import defaultdict
class Solution:
    def removeStonesUnionFind(self, stones: List[List[int]]) -> int:
        parent = {}            
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            parent[find(y)] = find(x)
            
        for i, j in stones:
            union(i, ~j)
            
        return len(stones) - len({find(x) for x in parent})
    def removeStonesDFS(self, stones: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)
        for i, j in stones:
            rows[i].add(j)
            cols[j].add(i)
            
        visitedRow, visitedCol = set(), set()
        
        def dfsRow(i):
            visitedRow.add(i)
            for j in rows[i]:
                if j not in visitedCol:
                    dfsCol(j)
        
        def dfsCol(j):
            visitedCol.add(j)
            for i in cols[j]:
                if i not in visitedRow:
                    dfsRow(i)
                    
        islands = 0
        for i, j in stones:
            if i not in visitedRow:
                islands += 1
                dfsRow(i)
                dfsCol(j)
        
        return len(stones) - islands