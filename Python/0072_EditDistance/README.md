# [72. Edit Distance](https://leetcode.com/problems/edit-distance)

## Description

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Example 1:

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

Example 2:

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Solution

The pseudocode of the algorithm shows below:

```
m, n = len(X), len(Y)

for i = 0 to m do
    T[i, 0] = i
for j = 0 to n do
    T[0, j] = j

for i = 0 to m do
    for j = 0 to n do
        if X[i-1] == Y[j-1] then
            T[i, j] = T[i-1, j-1]
        else
            T[i, j] = min(T[i-1, j], T[i-1, j-1], T[i, j-1]) + 1
return T[m, n]
```

We construct a matrix T with size of (m+1)(n+1) where m is the length of X and n is the length of Y and T[i, j] stores steps needed from substring X[0, i] to substring Y[0, j]. We first set value of elements in the first column with corresponding i because we need i steps to transform X[0, i] to empty string. We apply the same logic for the elements in the first row, we need j steps to transform empty string to Y[0, j]. And we go through every elements of T and calculate corresponding steps of T[i, j]. If X[i-1] == Y[j-1], we don’t need do anything so that the steps of T[i, j] is same as T[i-1, j-1]. If X[i-1] != Y[j-1], we find the min of T[i-1, j], T[i-1, j-1], and T[i, j-1] and plus 1. T[m, n] is the less steps needed to transform X into Y. 

## Related Topics

[String](https://leetcode.com/tag/string/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[One Edit Distance](https://leetcode.com/problems/one-edit-distance/), [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/), [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
