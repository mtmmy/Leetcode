using System;
namespace Leetcode.Solutions {
    public class MergeSortedArray {
        public void Solution(int[] nums1, int m, int[] nums2, int n) {
            var temp = new int[nums1.Length];

            var i = 0;
            var j = 0;
            var k = 0;

            while (i < m || j < n) {
                if (i < m && j < n) {
                    if (nums1[i] <= nums2[j]) {
                        temp[k] = nums1[i];
                        i++;
                        k++;
                    } else {
                        temp[k] = nums2[j];
                        j++;
                        k++;
                    }
                } else if (i < m) {
                    temp[k] = nums1[i];
                    i++;
                    k++;
                } else if (j < n) {
                    temp[k] = nums2[j];
                    j++;
                    k++;
                }
            }

            for (i = 0; i < nums1.Length; i++) {
                nums1[i] = temp[i];
            }
        }
    }
}

//[1,2,3,0,0,0,0]
//3
//[2,5,6]
//3