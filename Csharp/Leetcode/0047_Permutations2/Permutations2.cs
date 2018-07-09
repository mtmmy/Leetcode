using System;
using System.Collections.Generic;
using System.Linq;

namespace Leetcode.Solutions {
    public class Permutations2 {
        public IList<IList<int>> Solution(int[] nums) {
            var result = new List<IList<int>>();

            if (nums.Length == 0 || nums == null) {
                return result;
            }


            var used = Enumerable.Repeat(false, nums.Length).ToList();
            var list = new List<int>();
            GeneratePermutations(nums, used, list, result);
            return result;
        }

        void GeneratePermutations(int[] nums, List<bool> used, List<int> list, List<IList<int>> result) {
            if (list.Count == nums.Length) {
                result.Add(new List<int>(list));
                return;
            }

            for (int i = 0; i < nums.Length; i++) {
                if (used[i]) {
                    continue;
                }

                if (i > 0 && nums[i - 1] == nums[i] && !used[i-1]) {
                    continue;
                }

                used[i] = true;
                list.Add(nums[i]);
                GeneratePermutations(nums, used, list, result);
                used[i] = false;
                list.RemoveAt(list.Count - 1);
            }
        }
    }
}

//======
/* 
    //======
47. Permutations II
    //======
  Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
    //======
        This problem is similar to the problem #46. The difference is that there may be duplicates in this problem.
        However, the method we used in #46 cannot record wheather the value is used or not so that we cannot skip duplicate permutations.

        So we use a similar solution of problem #39, combination sum. We use a list to store each result and when the length of the list equals to the amount of input numbers, we store the list to the result.
        And we skip elements when 1. It has been used or 2. The value is same as the previous one and the previous one has not been used yet.
        By doing these, we can avoid duplicate permutations.

        Since the number of permutaions of N numbers is N!, the time complexity of finding all permutations is O(N!).
    //======
        Permutation, Recursion
    //======
        07/07/2018
    //======
        Leetcode
    //======
        https://leetcode.com/problems/permutations-ii/description/
    //======
*/