class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if num in d and d[num] > 0:
                result.append(num)
                d[num] -= 1
        
        return result