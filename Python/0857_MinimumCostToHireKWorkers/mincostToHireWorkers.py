from typing import List
from heapq import heappush, heappop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        totalQ, minPaid = 0, float('inf')
        heap = []
        for ratio, q in workers:
            totalQ += q
            heappush(heap, -q)
            if len(heap) > K:
                totalQ += heappop(heap)
            if len(heap) == K:
                minPaid = min(minPaid, totalQ * ratio)
        return minPaid