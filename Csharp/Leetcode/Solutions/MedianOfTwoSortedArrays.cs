using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {

    public class MedianOfTwoSortedArrays {

        public double Solution(int[] nums1, int[] nums2) {

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

            var pa = Math.Min(k / 2, m);
            var pb = k - pa;
            if (A[pa - 1] < B[pb - 1]) {
                int[] newA = SubArray(A, pa, A.Length - pa);
                return FindKth(newA, m - pa, B, n, k - pa);
            }

            if (A[pa - 1] > B[pb - 1]) {
                int[] newB = SubArray(B, pb, B.Length - pb);
                return FindKth(A, m, newB, n - pb, k - pb);
            }
            return A[pa - 1];
        }

        public int[] SubArray(int[] data, int index, int length) {
            int[] result = new int[length];
            Array.Copy(data, index, result, 0, length);
            return result;
        }
    }
}
