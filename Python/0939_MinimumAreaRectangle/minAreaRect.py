from typing import List
from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = len(set([x for x, y in points]))   # number of x values containing points
        ny = len(set([y for x, y in points]))   # number of y values containing points
        if n == nx or n == ny or nx == 1 or ny == 1:    # there must be at least both 2 for nx and ny to form a rectangle
            return 0
                
        pointDict = defaultdict(list)
        if nx > ny:
            for x, y in points:
                pointDict[x].append(y)
        else:
            for x, y in points:
                pointDict[y].append(x)
                
        lastX = {}
        result = float('inf')
        for x in sorted(pointDict):
            pointDict[x].sort()
            for i in range(len(pointDict[x])):
                for j in range(i):
                    y1, y2 = pointDict[x][j], pointDict[x][i]
                    # for a value x, there are y1 and y2 means there are two points (x, y1) and (x, y2)
                    # if there is x' where x' < x, we have another two points (x', y1) and (x', y2)
                    # we can from a rectangle by these 4 points
                    if (y1, y2) in lastX:
                        result = min(result, (x - lastX[(y1, y2)]) * (y2 - y1))
                    lastX[(y1, y2)] = x
        return 0 if result == float('inf') else result

    def minAreaRectBF(self, points: List[List[int]]) -> int:
        visited = set()
        result = float('inf')
        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y2) in visited and (x2, y1) in visited:
                    result = min(result, abs(x1 - x2) * abs(y1 - y2))
            visited.add((x1, y1))
        return 0 if result == float('inf') else result