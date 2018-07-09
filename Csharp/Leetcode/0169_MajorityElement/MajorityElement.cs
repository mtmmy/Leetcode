using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class MajorityElement {
        public int Solution(int[] nums) {

            var dictionary = new Dictionary<int, int>();
            var halfLength = nums.Length / 2;

            for (int i = 0; i < nums.Length; i++) {
                var num = nums[i];
                if (dictionary.ContainsKey(num)) {
                    dictionary[num]++;
                } else {
                    dictionary.Add(num, 1);
                }
                if (dictionary[num] > halfLength) {
                    return num;
                }
            }
            return -1;
        }
    }
}

//======
/* 
    //======
169. Majority Element
    //======
   Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
    //======
Go through the array once and use an extra space (space complexity is O(n)) to store the number of each numbers so that the time complexity is O(n).
    //======
        Array
    //======
        07/02/2018
    //======
        Leetcode
    //======
https://leetcode.com/problems/majority-element/description/
    //======
*/