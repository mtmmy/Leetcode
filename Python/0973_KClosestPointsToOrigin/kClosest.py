import heapq

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(K, points, key=lambda x: x[0] ** 2 + x[1] ** 2)

    def kClosest2(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        
        for p in points:
            heapq.heappush(heap, (p[0] ** 2 + p[1] ** 2, p))
            
        result = heapq.nsmallest(K, heap)
        return [p[1] for p in result]