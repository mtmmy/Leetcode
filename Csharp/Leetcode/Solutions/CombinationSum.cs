using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class CombinationSum {
        public IList<IList<int>> Solution (int[] candidates, int target) {

            var result = new List<IList<int>>();
            var subResult = new List<int>();

            CombinationSumDFS(candidates, target, 0, result, subResult);

            return result;
        }

        private void CombinationSumDFS (int[] candidates, int target, int start, List<IList<int>> result, List<int> subResult ) {
            if (target < 0) {
                return;
            }

            if (target == 0) {
                result.Add(new List<int>(subResult));
            } else {
                for (int i = start; i < candidates.Length; i++) {
                    subResult.Add(candidates[i]);
                    CombinationSumDFS(candidates, target - candidates[i], i, result, subResult);
                    subResult.RemoveAt(subResult.Count - 1);
                }
            }
        }
    }
}

//======
/* 
    //======
39. Combination Sum
    //======
  Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
    //======
    When we select a candidate candidate[i], we need to find all combination sum of ( target - cnadidate[i] ). 
    
    We use recursive function to find all combination and this function contains extra parameters such as 
    start which is the start index of the array of candidates, result which stored all of the results and subResult which is one of the result.
    This recursive function stops when the sum is greater than target.

    We start from the 0 of the candidates to the end and do not go back. And we only check for those number whose index is greater than the index of our current number in the recursive function.
    Since we don't look back for calculated candidates, the time complexity is O(NlogN).
    //======
        Recursion, Sum, Combination
    //======
        07/03/2018
    //======
        Leetcode
    //======
        https://leetcode.com/problems/combination-sum/description/
    //======
*/