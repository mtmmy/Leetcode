class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        d = {}
        
        for num in nums1:
            if num not in d:
                d[num] = 0
                
        for num in nums2:
            if num in d:
                result.append(num)
#         nums1.sort()
#         nums2.sort()
        
#         m = len(nums1)
#         n = len(nums2)
        
#         i, j = 0, 0
#         while i < m and j < n:            
#             if nums1[i] < nums2[j]:
#                 i += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 if nums1[i] not in result:
#                     result.append(nums1[i])
#                 i += 1
#                 j += 1                
        
        
        return list(set(result))