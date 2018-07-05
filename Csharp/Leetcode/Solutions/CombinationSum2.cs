using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class CombinationSum2 {
        public IList<IList<int>> Solution(int[] candidates, int target) {

            Array.Sort(candidates);

            var result = new List<IList<int>>();
            var subResult = new List<int>();

            CombinationSumDFS(candidates, target, 0, result, subResult, 0);

            return result;
        }

        private void CombinationSumDFS(int[] candidates, int target, int start, List<IList<int>> result, List<int> subResult, int level) {
            if (target < 0) {
                return;
            }

            if (target == 0) {
                result.Add(new List<int>(subResult));
            } else {
                for (int i = start; i < candidates.Length; i++) {
                    if (i > start && candidates[i] == candidates[i - 1]) {
                        continue;
                    }
                    subResult.Add(candidates[i]);
                    CombinationSumDFS(candidates, target - candidates[i], i + 1, result, subResult, level + 1);
                    subResult.RemoveAt(subResult.Count - 1);
                }
            }
        }
    }
}

//======
/* 
    //======
40. Combination Sum II
    //======
  Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
    //======
    It's similar to the #39. The only difference between #39 and this problem is that this problem can use a element only once.
    So we need to avoid the duplicate combinations. 
    In order to do this, we sort the array of candidates first because sorting is one of straightfoward way to eliminate duplicates.
    In each level of the recursive stack, if we met duplicate elements, we use only one of them to call recursive functions.
    By doing this, we can only take a solution which duplicate elements are comming from different levels and avoid duplicate results.

    The time complexity is same as #39 which is O(N!).
    
    //======
        Recursion, Sum, Combination
    //======
        07/04/2018
    //======
        Leetcode
    //======
    https://leetcode.com/problems/combination-sum-ii/description/
    //======
*/