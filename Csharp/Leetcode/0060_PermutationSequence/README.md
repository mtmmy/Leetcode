# [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence)

## Description

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

Given n and k, return the kth permutation sequence.

Note:

Example 1:

```
Input: n = 3, k = 3
Output: "213"
```

Example 2:

```
Input: n = 4, k = 9
Output: "2314"
```

## Solution

Let's take a look at all permutations when n = 4.

```
1234
1243
1324
1342
1423
1432
2134
2143
2314 
2341
2413
2431
3124
3142
3214
3241
3412
3421
4123
4132
4213
4231
4312
4321
```

We can observe that the number of appearances of each number at the left-most place is 6. And after the number at the left-most place has been decided, the number of appearances of each number at the second left-most place is 2. Where 6 = 3! and 2 = 2!. Depending on this rule, we can find the specific permutation we are looking for quickly. 

We create an array which stores values from 1! to (n-1)!. And we can get the left-most place by taking k divided by (n-1)!. Using n = 4 and k = 10 as the example. the left-most place will be 9/(3!) = 1. Index 1 of the number list is 2 and we remove 2 rom the number list. Then we take the remainder of the above divisor, we get 3 and do the same thing which is 3/(2!) = 1. Since 2 has been removed, index 1 is 3. We keep doing this until we run out of n.

The time complexity of this algorithm is O(n) and the space complexity is O(n).

## Related Topics

[Math](https://leetcode.com/tag/math/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Next Permutation](https://leetcode.com/problems/next-permutation/), [Permutations](https://leetcode.com/problems/permutations/)
