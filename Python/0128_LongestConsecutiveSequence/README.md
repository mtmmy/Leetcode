# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)

## Description

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

```
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

## Solution

To solve this problem, we first convert the input into a set which can eliminate duplicates and duplicates don't effect the answer at this problem. Then we go through the input list and we need to check if the number is in **numSet** because it may be removed. If the number is still in **numSet**, we start looking for its consecutive numbers which are plus one and minus one. For example, the number is 5, we check if 4 is in the set. If it is, we check 3. We keep checking minus one number until we don't find a such number in the **numSet** (do the similar step to plus one numbers). Since we are looking for consecutive numbers, when we find a number, we can safely remove it from **numSet**. Hence for each number we can find the length of its consecutive sequence and we keep the longest one which is our answer.

Converting a list to a set takes O(n). Finding numbers in a set is also O(n) since we remove numbers after we found it so every number will be visited just once. Totally, the algorithm costs O(n) computational time. The space complexity is O(n) as well.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Union Find](https://leetcode.com/tag/union-find/) 

## Similar Questions

[Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/)
