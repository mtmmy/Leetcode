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
            Array.Sort(nums);
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