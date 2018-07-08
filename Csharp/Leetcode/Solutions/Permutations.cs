using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class Permutations {
        
        public IList<IList<int>> Solution(int[] nums) {
            return GetPermutations(nums);
        }

        private List<IList<int>> GetPermutations(int[] nums) {

            var permutations = new List<IList<int>>();

            if (nums.Length < 2) {
                permutations.Add(new List<int>(nums));
            } else if (nums.Length == 2) {
                permutations.Add(new List<int>(new int[] { nums[0], nums[1] }));
                permutations.Add(new List<int>(new int[] { nums[1], nums[0] }));
            } else {
                var subNums = new int[nums.Length - 1];

                for (int i = 1; i < nums.Length; i++) {
                    subNums[i - 1] = nums[i];
                }

                var subPermutations = GetPermutations(subNums);

                foreach (List<int> p in subPermutations) {
                    for (int i = 0; i < p.Count + 1; i++) {
                        var permu = new List<int>(p);
                        permu.Insert(i, nums[0]);
                        permutations.Add(permu);
                    }
                }
            }

            return permutations;
        }
    }
}

//======
/* 
    //======
46. Permutations
    //======
  Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
    //======
    Combination of Permutation, for these kinds of problems, we generally use recursion to solve them.
    For this problem, we use a recursive function. For looking for all permutations of N elements, we alredy have all permutations of (N-1) elements, 
    so we just insert N-th element to every index of all permutations of (N-1) elements.    
    For example, we are looking for permutations of [1, 2, 3], so we already have permuations of [2, 3] which are [2, 3] and [3, 2].
    And we insert 1 into gaps of each array.
    For [2, 3], after insertion, we get [1, 2, 3], [2, 1, 3] and [2, 3, 1].
    For [3, 2], after insertion, we get [1, 3, 2], [3, 1, 2] and [3, 2, 1].

    Since the number of permutaions of N numbers is N!, the time complexity of finding all permutations is O(N!).
    //======
        Permutation, Recursion
    //======
        07/06/2018
    //======
        Leetcode
    //======
        https://leetcode.com/problems/permutations/description/
    //======
*/