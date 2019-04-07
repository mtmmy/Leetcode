from typing import List
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        islandSet = set()
        visited = set()
        
        def formIsland(i, j, d, shape):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid[i][j] == 0:
                return
            visited.add((i, j))
            shape.append(d)
            formIsland(i + 1, j, "d", shape)
            formIsland(i - 1, j, "u", shape)
            formIsland(i, j + 1, "r", shape)
            formIsland(i, j - 1, "l", shape)
            shape.append("s")
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = []
                    formIsland(i, j, "s", shape)              
                    islandSet.add("".join(list(map(str, shape))))
        return len(islandSet)
                    