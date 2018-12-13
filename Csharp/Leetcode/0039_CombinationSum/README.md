# [39. Combination Sum](https://leetcode.com/problems/combination-sum)

## Description

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

Example 1:

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

Example 2:

```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

## Solution

We use DFS to look for all the combinations. For every time in DFS function, we choose one number as the canditate and **new target** which is **old_target - candidate** to start a new DFS function. Once the target reaches zero, we get a combination whose sum is the **target** from the original question and store such a combination. Another scenario is that the new target is smaller than zero, which means this combination dosen't satisify the requirement. We simply stop going deeper in DFS.

Since our solution is based on DFS, we can visialize this algorithm to a tree structure where the height of the tree is linear to the **target** denoted to **h** and the branch of each node is **n** (number of candidates). The time we need to traverse the whole tree is O(n<sup>t</sup>). Space complexity is the height of the tree which is O(h).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/), [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/), [Combinations](https://leetcode.com/problems/combinations/), [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/), [Factor Combinations](https://leetcode.com/problems/factor-combinations/), [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
