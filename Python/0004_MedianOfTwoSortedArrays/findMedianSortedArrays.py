class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findKth(A, m, B, n, k):
            if m > n:
                return findKth(B, n, A, m, k)
            
            if m == 0:
                return B[k - 1]
            
            if k == 1:
                return min(A[0], B[0])

            idxA = min(k // 2, m)
            idxB = k - idxA

            if A[idxA - 1] < B[idxB - 1]:
                return findKth(A[idxA:], m - idxA, B, n, k - idxA)
            
            if A[idxA - 1] > B[idxB - 1]:
                return findKth(A, m, B[idxB:], n - idxB, k - idxB)

            return A[idxA - 1]
            
        total = len(nums1) + len(nums2)
        if total % 2 == 0:
            return (findKth(nums1, len(nums1), nums2, len(nums2), total // 2) + findKth(nums1, len(nums1), nums2, len(nums2), total // 2 + 1)) / 2
        else:
            return findKth(nums1, len(nums1), nums2, len(nums2), total // 2 + 1)

if __name__ == "__main__":
    target = Solution()
    print(target.findMedianSortedArrays([1,2], [6,7,8,9,10,11,12]))