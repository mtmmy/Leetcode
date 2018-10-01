using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {

    public class MedianOfTwoSortedArrays {

        public double FindMedianSortedArrays(int[] nums1, int[] nums2) {

            var total = nums1.Length + nums2.Length;
            if (total % 2 == 0) {
                return (FindKth(nums1, nums1.Length, nums2, nums2.Length, total / 2) + FindKth(nums1, nums1.Length, nums2, nums2.Length, total / 2 + 1)) / 2;
            } else {
                return FindKth(nums1, nums1.Length, nums2, nums2.Length, total / 2 + 1);
            }
        }

        public double FindKth(int[] A, int m, int[] B, int n, int k) {

            if (m > n) {
                return FindKth(B, n, A, m, k);
            }

            if (m == 0) {
                return B[k - 1];
            }

            if (k == 1) {
                return Math.Min(A[0], B[0]);
            }

            var idxA = Math.Min(k / 2, m);
            var idxB = k - idxA;
            if (A[idxA - 1] < B[idxB - 1]) {
                int[] newA = SubArray(A, idxA, A.Length - idxA);
                return FindKth(newA, m - idxA, B, n, k - idxA);
            }

            if (A[idxA - 1] > B[idxB - 1]) {
                int[] newB = SubArray(B, idxB, B.Length - idxB);
                return FindKth(A, m, newB, n - idxB, k - idxB);
            }
            return A[idxA - 1];
        }

        public int[] SubArray(int[] data, int index, int length) {
            int[] result = new int[length];
            Array.Copy(data, index, result, 0, length);
            return result;
        }
    }
}
