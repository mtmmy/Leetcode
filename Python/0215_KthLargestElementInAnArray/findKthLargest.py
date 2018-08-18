import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort(reverse=True)
        # return nums[k - 1]
        
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if heap[0] < num:
                heapq.heapreplace(heap, num)
                
        return heap[0] if heap else None