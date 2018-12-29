class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, write = m - 1, n - 1, m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[write] = nums2[j]
                j -= 1
            else:
                nums1[write] = nums1[i]                
                i -= 1
            write -= 1
        
        nums1[:j + 1] = nums2[:j + 1]