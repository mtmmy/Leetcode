import collections
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums1)        
        result = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                result.append(num)
                counter[num] -= 1
        
        return result
    
    def intersect2(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result