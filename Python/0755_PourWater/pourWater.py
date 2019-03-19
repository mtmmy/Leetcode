from typing import List
from heapq import heappush, heappop
# class LeftCylindar:
#     def __init__(self, i, heights):
#         self.idx = i
#         self.height = heights[i]
#     def __lt__(self, other):
#         if self.height != other.height:
#             return self.height < other.height
#         return self.idx > other.idx

# class RightCylindar:
#     def __init__(self, i, heights):
#         self.idx = i
#         self.height = heights[i]
#     def __lt__(self, other):
#         if self.height != other.height:
#             return self.height < other.height
#        return self.idx < other.idx

class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        i, j = K - 1, K + 1
        heapLeft, heapRight = [], []        
        
        for drop in range(V):
            while i >= 0 and heights[i] <= heights[i + 1]:
                heappush(heapLeft, (heights[i], -i))
                i -= 1
            while j < len(heights) and heights[j] <= heights[j - 1]:
                heappush(heapRight, (heights[j], j))
                j += 1
            if heapLeft and heapLeft[0][0] < heights[K]:
                idx = -heappop(heapLeft)[1]
                heights[idx] += 1
                heappush(heapLeft, (heights[idx], -idx))
            elif heapRight and heapRight[0][0] < heights[K]:
                idx = heappop(heapRight)[1]
                heights[idx] += 1
                heappush(heapRight, (heights[idx], idx))
            else:
                heights[K] += 1
        return heights
    
    def pourWater2(self, heights: List[int], V: int, K: int) -> List[int]:
        for i in range(V):
            cur = K
            while cur > 0 and heights[cur] >= heights[cur - 1]:
                cur -= 1
            while cur < len(heights) - 1 and heights[cur] >= heights[cur + 1]:
                cur += 1
            while cur > K and heights[cur] >= heights[cur - 1]:
                cur -= 1
            heights[cur] += 1
        return heights