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